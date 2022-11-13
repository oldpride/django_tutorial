from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# run makemigrations and migrate after changing models, so that database is updated. -tian
# 'makemigrations' will generate sql under blog/migrations/0001_initial.py
# "sqlmigrate blog 0001' will print out its corresponding sql
# 'migrate' will run the sql

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() # TextField can be multilines, unrestricted -tian
    date_posted = models.DateTimeField(default=timezone.now)
    # date_posted = models.DateTimeField(auto_now_add=True) but this will not allow modify -tian
    # timezone.now is the function name. because we don't want to call it now, we don't use timezone.now(). -tian
    # last_updated = models.DateTimeField(auto_now=True) -tian
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if user is deleted, so will be the post -tian

    def __str__(self):
        return self.title

    # once we created the post, we need to tell django where to redirect - by define get_absolute_url() -tian
    def get_absolute_url(self):
        # redirect() vs reverse() -tian
        #   redirect() will direct you to a specific route defined in urls.py. example: users/views.py
        #   reverse() will simply return the url to that route as a string
        return reverse('post-detail', kwargs={'pk': self.pk})
        # 'post-detail' is defined in blog/urls.py -tian
