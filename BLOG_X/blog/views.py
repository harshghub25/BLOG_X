from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment, Like, Follow, Category, Tag
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
class PostListView(generic.ListView):
    model = Post
    paginate_by = 6
    template_name = 'blog/post_list.html'
    def get_queryset(self):
        qs = Post.objects.select_related('author','category').order_by('-created')
        # filters (author, category, date range)
        author = self.request.GET.get('author')
        cat = self.request.GET.get('category')
        if author:
            qs = qs.filter(author__username=author)
        if cat:
            qs = qs.filter(category__slug=cat)
        return qs
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title','slug','content','cover','category','tags']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    fields = ['title','slug','content','cover','category','tags']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_staff
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_staff
@login_required
def toggle_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('post_detail', slug=slug)
@login_required
def toggle_follow(request, username):
    target = get_object_or_404(User, username=username)
    if target == request.user:
        return redirect('post_list')
    obj, created = Follow.objects.get_or_create(follower=request.user, following=target)
    if not created:
        obj.delete()
    return redirect('post_list')
