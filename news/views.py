from django.views.generic import ListView, DetailView
from .models import *

class NewsList(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'

# дженерик для получения деталей новости
class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'new'
    permission_required = 'news.add_post'
