from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from myapp.models import Posts,Comments,CommentsReply,PostReact
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from .forms import *

class LoginPageView(LoginView):
    template_name = "login.html"
    success_url = "/home/"

class ProfilePageView(TemplateView):
    template_name = 'profile.html'

class LogoutPageView(LogoutView):
    next_page = '/login/'
    
class PasswordChangePageView(PasswordChangeView):
    template_name = "password_change.html"
    success_url = "/login/"

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Django Learning" 
        context["desc"] = "A paragraph generator is an AI-writing software that can take minimal text input and create an entire paragraph. With recent advances in natural language processing (NLP) and" 
        context["price"] = 100
        return context

class PostsPageView(ListView):
    model = Posts
    context_object_name = 'posts'
    template_name='home.html'
    
class PostReactView(View):
    def get(self, request, *args, **kwargs):
        post_id = self.kwargs['pk']
        react = request.GET.get('react')
        current_post = Posts.objects.get(id=post_id)
        if react == 'LIKE':
            PostReact.objects.create(post=current_post,post_react='LIKE')
        elif react == 'LOVE':
            PostReact.objects.create(post=current_post,post_react='LOVE')
        elif react == 'SAD':
            PostReact.objects.create(post=current_post,post_react='SAD')
        elif react == 'CARE':
            PostReact.objects.create(post=current_post,post_react='CARE')
        else:
            pass
        return redirect("/home/")
    
class PostsDetailPageView(DetailView):
    model = Posts
    # context_object_name = 'post'
    template_name='details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_post = self.get_object()
        context["form"] = CommentForm(post = self.object)
        context['allcomment'] = Posts.objects.get(pk=current_post.pk)
        
        li,lo,sa,ca= 0,0,0,0
        for react in self.object.postreact_set.all():
            if react.post_react == 'LOVE':
                lo+=1
            elif react.post_react == 'LIKE':
                li+=1
            elif react.post_react == 'SAD':
                sa+=1
            else:
                ca+=1
        context['li'] = li
        context['lo'] = lo
        context['sa'] = sa
        context['ca'] = ca
        context['all_'] = lo+li+sa+ca
        return context

    def post(self, request,*args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST,post=post)
        if form.is_valid():
            form.save()
            return redirect(f"/post/{post.pk}/")
        else:
            return self.render_to_response({'form':form,'post':post})
    
class PostsAddPageView(CreateView):
    model = Posts
    fields = ["title","content"]
    template_name='add.html'
    success_url = "/post/add/"
    
class PostsUpdatePageView(UpdateView):
    model = Posts
    template_name='update.html'
    fields = ["title","content"]
    success_url = "/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Posts.objects.get(id=self.kwargs['pk']) 
        return context
    
    
class PostsDeletePageView(DeleteView):
    model = Posts
    template_name='posts_confirm_delete.html'
    success_url = "/home/"

class CommentReplyView(CreateView):
    model = CommentsReply
    fields = ["reply"]
    template_name='reply.html'
    success_url = "/"
    
    def post(self, request,*args, **kwargs):
        comment = Comments.objects.get(comment=self.kwargs['title'])
        form = CommentReplyForm(request.POST)
        if form.is_valid():
            form.instance.comment = comment
            form.save()
            return redirect("/")
        else:
            return self.render_to_response({'form':form})