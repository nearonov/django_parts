from django.views.generic import DetailView
from articles.models import Article


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article.html'
