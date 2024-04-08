from django.shortcuts import redirect, render
from django.views import View
from posts.models import Post
from django.contrib import messages
# Create your views here.

class PostList(View):
    template_name =  'posts/post_list.html'

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts':posts
        }
        return render(request, self.template_name, context)

class CreatePost(View):
    template_name = 'posts/post_form.html'
    success_url = 'posts:all_posts'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        Post.objects.create(
            title = request.POST.get('title'),
            text = request.POST.get('text')
        )
        return redirect(self.success_url)