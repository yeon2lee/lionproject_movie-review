from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Review(models.Model):
    post_title = models.CharField(max_length=100, default="제목없음")
    movie_title = models.CharField(max_length=100, default="제목없음")
    author = models.CharField(max_length=100, default="글쓴이없음")
    pub_date = models.DateTimeField()
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='review/', blank=True, null=True)
    image_thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(250, 230)])

    def __str__(self):
        return self.post_title

    def summary(self):
        return self.body[:30]

class Comment(models.Model):
    post_id = models.ForeignKey("Review", on_delete=models.CASCADE, db_column="post_id")
    comment_id = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    author = models.CharField(max_length=10, default="")
    body = models.TextField(default="")