from tastypie.resources import ModelResource
# for converting Models into a web resource
from tastypie.constants import ALL
# allows us set kind of query type 
# that we can perform on our models
from models import Article 

class ArticleResource(ModelResource):
    # Decalre resource is by creating a class and derive ot from model 
    # resource and create a webservice from it.
    class Meta: # extra infromation about the resource
        queryset = Article.objects.all() # get everthing from database.
        resource_name = 'article'
        # When this service is called on our url its name will be called
        # in other words it will invoke this api when called, 
        # http:localhost/atricles/api/
        filtering = {'title':ALL}
        # by this we can configure how we would like to filter the API.
    
