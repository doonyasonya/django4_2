from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy

from blog.models import Category, Comment, Post


class IndexListView(ListView):
    model = Post
    ordering = 'id'
    template_name = 'blog/index.html'
    paginate_by = 5


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:profile')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/create.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.object.Post
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/detail.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category.html'


class ProfileListView(IndexListView):

    template_name = 'blog/profile.html'
    author = None


class CommentCreateView(LoginRequiredMixin, CreateView):
    birthday = None
    model = Comment

    def dispatch(self, request, *args, **kwargs):
        self.birthday = get_object_or_404(Comment, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:comment', kwargs={'pk': self.post.pk})
