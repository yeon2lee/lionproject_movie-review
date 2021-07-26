from django.db import models

class Review(models.Model):
    post_title = models.CharField(max_length=100, default="제목없음")
    movie_title = models.CharField(max_length=100, default="제목없음")
    author = models.CharField(max_length=100, default="글쓴이없음")
    pub_date = models.DateTimeField()
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='review/', blank=True, null=True)

    def __str__(self):
        return self.post_title

    def summary(self):
        return self.body[:30]