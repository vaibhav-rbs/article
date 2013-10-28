from django.conf.urls import patterns,include,url
from api import ArticleResource

article_resource = ArticleResource()#Create an instance of it

urlpatterns = patterns('',
    url(r'^all/$','article.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$','article.views.article'),
    url(r'^language/(?P<language>[a-z\-]+)/$','article.views.language'),
    url(r'^create/$','article.views.create'),
    url(r'^like/(?P<article_id>\d+)/$','article.views.like_article'),
    url(r'^add_comment/(?P<article_id>\d+)/?$','article.views.add_comment'),
    url(r'^search/$','article.views.search_titles'),
    # TODO DELETE when fixed'articles/all/article/search/'
    # url(r'^all/article/search/$','article.views.search_titles'),
    url(r'^api/',include(article_resource.urls)), 
    # urls are automatically generated by the inherted class,
    # this one line contains all the urls that can be 
    # made using this include Model resource class generates
    # the all the urls
)
