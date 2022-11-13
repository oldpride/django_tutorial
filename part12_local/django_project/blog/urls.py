from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    # don't generic name 'home' to avoid ambiguity -tian
    # path('', views.home, name='blog-home'),
    #
    # PostListView default template is <app>/<model>_<viewtype>.html, or blog/Post_List.html
    # in blog/views.py, we set template_name = 'blog/home.html'
    path('', PostListView.as_view(), name='blog-home'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # pk is primary key, -tian
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'), # views.py about()
]
