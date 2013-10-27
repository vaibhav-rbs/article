"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from article.models import Article,get_upload_file_name
from django.utils import timezone
from time import time
from django.core.urlresolvers import reverse

class ArticleTest(TestCase):
    def create_article(self,title="test title",body = "test body"):#helper function
        return Article.objects.create(title=title,body=body,pub_date=timezone.now(),likes=0)
    

    def test_article_creation(self): #must have test_<something>
        a = self.create_article()
        self.assertTrue(isinstance(a,Article))
        self.assertEqual(a.__unicode__(),a.title)


    def test_get_upload_file_name(self):
        filename = "testfile"
        path = "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)

        created_path = get_upload_file_name(self,filename)
        
        self.assertEqual(path,created_path)
    
    
    def test_article_list_view(self):
        a = self.create_article()
        url = reverse('article.views.articles')
        resp = self.client.get(url)#TestCase class has inbuilt browser known as client which can visit urls
        
        self.assertEqual(resp.status_code,200)# Equates the output of the status_code to 200
        self.assertIn(a.title,resp.content)#checks if the value class article's title is in massive chunk of content
    
    def test_article_detail_view(self):
        a = self.create_article()
        url = reverse('article.views.article',args=[a.id])# use this when you have a parameter in your url
        resp = self.client.get(url)
        
        self.assertEqual(reverse('article.views.article',args=[a.id]),a.get_absolute_url())
        self.assertEqual(resp.status_code,200)
        self.assertIn(a.title,resp.content)        
        
