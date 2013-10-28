from django.shortcuts import render_to_response
from article.models import Article, Comment
from django.http import HttpResponse
from form import ArticleForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone


def articles(request): 
    language = 'en-us'
    session_language = 'en-us'
    
    if 'lang' in request.COOKIES:
	language = request.COOKIES['lang']
	
    if 'lang' in request.session:
	session_language = request.session['lang']
	
    args ={}
    args.update(csrf(request))
    
    args['articles'] = Article.objects.all()
    args['language'] = language
    args['session_language'] = session_language

    return render_to_response('articles.html',args)

def article(request,article_id =1):
    return render_to_response('article.html',
			     {'article': Article.objects.get(id = article_id)})

def language(request,language = 'en-us'):
    response = HttpResponse("setting langauge to %s" %language)
    
    response.set_cookie('lang',language)
    # Cookie is a HttpResponse object
    
    request.session['lang'] = language
    # Session is a HttpRequest object
    
    return response
    
def create(request):
    if request.POST:
	form = ArticleForm(request.POST,request.FILES)
        # Request.files is for uploading a files
	if form.is_valid():
	    form.save()
			
	    return HttpResponseRedirect('/articles/all')
		
    else:
	form = ArticleForm()
		
    args ={}
    args.update(csrf(request))
		
    args['form'] = form
		
    return render_to_response('create_article.html',args)
	
def like_article(request,article_id):
	if article_id:
	    a = Article.objects.get(id=article_id)
	    count = a.likes
	    count += 1
	    a.likes = count
	    a.save()
	
	return HttpResponseRedirect('/articles/get/%s' % article_id )
    
def add_comment(request,article_id):
    a = Article.objects.get(id=article_id)
    
    if request.method == "POST":
	f =CommentForm(request.POST)
	if f.is_valid():
		# This means that save this instance of form but do not
                # push anything to databases(commit = False) as we are 
                # not finished yet
	    c = f.save(commit =False)
	    c.pub_date = timezone.now()
	    c.article = a 
	    c.save()
            # by default commit = True, therefore the comment will be 
            # saved to the database.
	    
	    return HttpResponseRedirect('/articles/get/%s' % article_id )
    else:
	f = CommentForm()
	    
    args = {}
    args.update(csrf(request))
    args['article'] = a
    args['form'] = f
	    
    return render_to_response('add_comment.html',args)

def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
	search_text = ''
    
    articles = Article.objects.filter(title__contains=search_text) 

    return render_to_response('ajax_search.html',{'articles':articles})
