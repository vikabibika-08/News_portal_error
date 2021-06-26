from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from news.models import *

class Author(models.Model):  # наследуемся от класса Model
    authors = models.OneToOneField(User, on_delete = models.CASCADE)
    authors_rating = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')
        commentRat = self.authors.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')
        self.authors_rating = pRat *3 +cRat
        self.save()

class Category(models.Model):
    category_name = models.CharField(max_length=65, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    NEWS = 'NP'
    ARTICLE_POST = 'AP'
    POST_TYPES = (
        (NEWS, 'Новость'),
        (ARTICLE_POST, 'Статья'),
    )
    post_category_type = models.CharField(max_length=2, choices=POST_TYPES, default=ARTICLE_POST)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    create_datetime = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=128)
    content = models.TextField()
    rating = models.SmallIntegerField(default=0)
    def like(self):
        self.rating +=1
        self.save()
    def dislike(self):
        self.rating -=1
        self.save()
    def preview(self):
        return self.content[0:123] + "..."


class PostCategory(models.Model):
    postcategory_informationThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    postcategoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_datetime = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -=1
        self.save()