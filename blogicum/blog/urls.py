from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path(
        'posts/create/',
        login_required(views.PostCreateView.as_view()),
        name='create_post'
    ),
    path(
        'posts/<int:post_id>/edit',
        login_required(views.PostUpdateView.as_view()),
        name='edit_post'
    ),
    path(
        'posts/<int:post_id>/',
        login_required(views.PostDetailView.as_view()),
        name='post_detail'
    ),
    path(
        'posts/delete/',
        login_required(views.PostDeleteView.as_view()),
        name='delete_post'
    ),
    path(
        'category/<slug:category>/',
        login_required(views.CategoryListView.as_view()),
        name='category_posts'
    ),
    path(
        'profile/<slug:username>/',
        login_required(views.ProfileListView.as_view()),
        name='profile'
    ),
]
