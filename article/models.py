from django.conf import settings
from whoosh import store, fields, index
import os.path
from whoosh.index import create_in,open_dir
from django_test import settings
from django.db import models
from time import time # for form time stamp

def get_upload_file_name(instance, filename):
    return settings.UPLOAD_FILE_PATTERN % (str(time()).replace('.','_'), filename)

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date publised')
    likes = models.IntegerField(default =0)
    # get_upload_file_name is a function
    thumbnail = models.FileField(
        upload_to=get_upload_file_name, null=True, blank=True
        )
    
    def __unicode__(self):
        return(self.title)
    
    def get_absolute_url(self):
        return "/articles/get/%i/" % self.id
        
    def get_thumbnail(self):
        thumb = str(self.thumbnail)
        if not settings.DEBUG:
            thumb = thumb.replace('assets/', '')
            
        return thumb
   
    
class Comment(models.Model):
    name = models.CharField(max_length=200)
    #first_name = models.CharField(max_length=200)
    #second_name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date publised')
    article = models.ForeignKey(Article,null=True, blank=True)
    
    ''' for Fixtures use python manage.py dumpdata article 
    --indent=4 > article.json #this puts the data into .json
    file call article.json to check if everthing is ok
    use python manage.py sqlclear article #for clearing the tables 
    and data with old schema use python manage.py dbshell for creating
    new tables articles and comments use python manage.py loaddata 
    article.json #for uploading data from fixtures to the database  '''
 
    
