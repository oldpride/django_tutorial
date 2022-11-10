from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

# Hard-coded html -tian
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse('<h1>About Page</h1>')

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# called by blog/urls.py
class PostListView(ListView):
    model = Post # this corresponds to blog/models Post class -tian
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # variable name in template html -tian
    ordering = ['-date_posted'] # without '-', 'data_posted' would be oldest-to-newest, -tian
    paginate_by = 5 # used by blog/templates/blog/home.html


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        # if the user exists, we get the user; otherwise, we return 404 (page not found) -tian
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

# LoginRequiredMixin needs to the first in the list -tian
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # author is a foreign key (blog/models.py), therefore is required to set -tian
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # test_func() is called by serPassesTestMixin -tian
    # this prevents user from updating posts not authored by him/her -tian
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    # upon delete success, we go to this URL
    # delete will fail without this URL.
    # delete operation is either all (success) or nothing (done).
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    # todo: how to add a message.success() like it in users/views.py -tian


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
