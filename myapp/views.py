from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from myapp.models import Posts

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
    
class PostsDetailPageView(DetailView):
    model = Posts
    context_object_name = 'post'
    template_name='details.html'
    
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
    
class PostsDeletePageView(DeleteView):
    model = Posts
    template_name='posts_confirm_delete.html'
    success_url = "/"
    
