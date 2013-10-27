# Allow us to render a template back to the browser.
from django.shortcuts import render_to_response
# Allows to redirect the browser to diffrent URL'S.  
from django.http import HttpResponseRedirect 
# Takes care of checking user name and password and confirming that user is logged in or else logging them out.
from django.contrib import auth 
# csrf is used for Web security which is a method to prevent Hacking. To inject new variables automatically into the context of a template, context processors are used. Context processors run before the template is rendered and have the ability to inject new values into the template context. A context processor is a function that returns a dictionary. 
from django.core.context_processors import csrf 
# This is already created forms made for user registaration
# from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm
# we are using Sessionwizard view for transmitting the information along the pages
from django.contrib.formtools.wizard.views import SessionWizardView
# we will be sending mails using send_mail library
from django.core.mail import send_mail
#import logging
#logr = logging.getlogger(__name__)

def login(request):
    # create a dict 'c'
    c = {} 
    # push csrf object
    c.update(csrf(request))
    # pass c dict to HTML page
    return render_to_response('login.html',c)

def auth_view(request):
	# goes into the request and looks for POST dict information from the 
        # form and gets username and password,notice there is a default empty string
	# the empty string is for the case if there is no value for user name 
        # and password as it does not exist yet then we will have empty string returned i        # n the variable as get method breaks when we dont have a value, 
        # Basically its a nice way of saying if you dont find something then return 
        # something nicer instead of breaking the code.   
    username = request.POST.get('username','') 
    password = request.POST.get('password','')
    # it is the main check, use authenticate method of auth object and pass it
    # to username and password variables and this will go in and check if user
    # exist. If user does exists then it will return a user object if there is 
    # no match then it returns None, authenticate does not log the user in it just 
    # checks the user existence. 
    user = auth.authenticate(username= username,password=password)
    
    if user is not None:
    	# if there is a user then use the auth object and log the user in the system using login method
        auth.login(request,user)
        # use HttpResponseRedirect object so that the browser is redirected to 
        # the url 'accounts/loggedin' which will execute loggedin view which is
        # defined right after this view   
        return HttpResponseRedirect('/accounts/loggedin') 
        # if user is not found then, use HttpResponseRedirect object so that 
        # the browser is redirected to the url 'accounts/invalid' which will execute 
        # invalid_login view which is defined right after this loggedin view 
    else:
       return HttpResponseRedirect('/accounts/invalid')
	# loggedin basically renders loggedin.html and passes thru the full_name 
        # variable which we embed insdie the loggedin.html page
def loggedin(request):
	# request.user has various properties and username is one of them
    return render_to_response('loggedin.html',
                              {'full_name':request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
	# auth has a method called log out for logging out the user and rendering 
        # the logout.html file
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
	# If the form has been submitted...
    if request.method == "POST":
    	# form = UserCreationForm(request.POST)
    	# we are going to pass the values of request.POST a dictionary to 
        # UserCreationForm and create a form object
    	# A form bound to the POST data
        form = MyRegistrationForm(request.POST)
        # if form is validated then the form object should be saved 
        # with the resgitration information of the new user 
        if form.is_valid():
            form.save()
            # now HttpResponseRedirect takes us to  url(r'^accounts/register_success/$','django_test.views.register_success')
            # now accounts/register_success/ causes the excution of django_test.views.register_success views
            return HttpResponseRedirect('/accounts/register_success')
    
    # for security purpose we have to embedd csrf tokens into agrs which will help us to know this post
    # method is coming from a reliable source 
        
    args={}
    args.update(csrf(request))
    # now we are embedding a blank user creation form into the args, it has no information put in it
    args['form'] = MyRegistrationForm()
    print args
    return render_to_response('register.html',args)

def register_success(request):
    return render_to_response('register_success.html')    


# IMPORTANT: when we use auth method in our
# views we have to do syncdb for making 
# corresponding DB tables thats deals with 
#the user, for storing thier name,passwrod email

# we have to use Session Wizard which is a class 
# based view as we cannot use fucntion based views

class ContactWizard(SessionWizardView):
    template_name = "contact_form.html"
    
    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        
        return render_to_response('done.html', {'form_data': form_data})
    
    
def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    
    #logr.debug(form_data[0]['subject'])
    #logr.debug(form_data[1]['sender'])
    #logr.debug(form_data[2]['message'])
    
    send_mail(form_data[0]['subject'], 
              form_data[2]['message'], form_data[1]['sender'],
              ['vaibhav.rbs@gmail.com'], fail_silently=False)
    
    
    return form_data	
	
	
