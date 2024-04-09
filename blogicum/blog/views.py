from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post
from core.constants import MAX_POSTS_ON_SCREEN


def index(request):
    post_list = (
        Post.objects.select_related(
            'author',
            'location',
            'category'
        )
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        )[:MAX_POSTS_ON_SCREEN]
    )
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related(
            'author',
            'location',
            'category'
        ),
        pk=post_id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category):
    post_category = get_object_or_404(
        Category,
        slug=category,
        is_published=True
    )
    post_list = (
        Post.objects.select_related(
            'author',
            'location',
            'category'
        )
        .filter(
            category=post_category,
            is_published=True,
            pub_date__lte=timezone.now()
        )
    )
    return render(
        request,
        'blog/category.html',
        {
            'category': post_category,
            'post_list': post_list
        }
    )
