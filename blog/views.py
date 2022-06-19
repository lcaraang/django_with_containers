from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from django.shortcuts import redirect
from django.utils import timezone
from django.db.models import Q

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """Return all posts."""
        return Post.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'posts/create.html'
    model = Post
    fields = ['author', 'title', 'text']
    success_url = reverse_lazy('posts:index') # more robust than hardcoding to /posts/; directs user to index view after adding a post

class UpdateView(generic.edit.UpdateView):
    template_name = 'posts/update.html'
    model = Post
    fields = ['author', 'title', 'text']
    success_url = reverse_lazy('posts:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'posts/delete.html' # override default of posts/post_confirm_delete.html
    model = Post
    success_url = reverse_lazy('posts:index')

def publish(request, pk):
        Post.objects.get(pk=pk).publish()
        return redirect(request.META['HTTP_REFERER'])

class OrderedView(generic.ListView):
    template_name = 'posts/ordered.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.order_by('title')

class FilteredView(generic.ListView):
    template_name = 'posts/filtered.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(~Q(published_date__lte=timezone.now()))

class FilteredOrderedView(generic.ListView):
    template_name = 'posts/filtered-ordered.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


        
        

