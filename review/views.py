from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q # 검색 기능을 위해 추가
from .models import Review
from .forms import ReviewForm

def home(request):
    reviews = Review.objects.all()
    reviews_list = Review.objects.all()
    paginator = Paginator(reviews_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'reviews':reviews, 'posts':posts})

def detail(request, id):
    review = get_object_or_404(Review, pk = id)
    return render(request,'detail.html',{'review':review})

def new(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.pub_date = timezone.now()
            new_review.save()
            return redirect('detail', new_review.id)
        return redirect('home')
    else:
        form = ReviewForm()
        return render(request, 'new.html', {'form':form})

def edit(request, id):
    update_review = get_object_or_404(Review, pk = id)
    if request.method == 'POST':
        edit_form = ReviewForm(request.POST, request.FILES, instance = update_review)
        if edit_form.is_valid():
            update_review = edit_form.save(commit = False)
            update_review.pub_date = timezone.now()
            update_review.save()
        return redirect('/review/detail/' + str(id))
    else:
        edit_form = ReviewForm(instance = update_review)
        return render(request, 'edit.html', {'edit_form':edit_form})

def delete(request, id):
    delete_review = Review.objects.get(id = id)
    delete_review.delete()
    return redirect('home')

def search(request):
    search_review = Review.objects.all().order_by('-id')

    query = request.POST.get('query', "") 

    if query:
        search_review = search_review.filter(
            Q(post_title__icontains=query) |  # 글제목 검색
            Q(movie_title__icontains=query) | # 영화제목 검색
            Q(author__icontains=query) |  # 저자검색
            Q(body__icontains=query)  # 내용검색
        ).distinct() # distinct()는 중복 방지를 위해서 추가
        return render(request, 'search.html', {'search_review' : search_review, 'query' : query})
    
    else:
        return render(request, 'search.html')