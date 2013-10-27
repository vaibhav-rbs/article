# allow us to render a template back to the browser.
from django.shortcuts import render_to_response
# allows to redirect the browser to diffrent URL'S.  
from django.http import HttpResponseRedirect 
# csrf is used for Web security which is a method to prevent Hacking.
# To inject new variables automatically into the context of a template,
# context processors exist are used. Context processors run before the 
# template is rendered and have the ability to inject new values into 
# the template context. A context processor is a function that returns
# a dictionary. 
from django.core.context_processors import csrf 
# import UserProfiles from userprofile app
from forms import UserProfileForm
# they allow you to add functionality for function you've already
# created so that you can extend the functionality without necessarily 
# writing lot of lines 
from django.contrib.auth.decorators import login_required
# while when we define our function we use @login_required just before 
# we define the function and this attaches to user_profile function and 
# automatically in the background it checks wheather the user is logged
# in, if the user is not logged in then this automatically redirects to
# login page and all this is achived by @login_required, Bloody simple.
# This is done to make some of the views secure 

@login_required
def user_profile(request):
    if request.method == "POST":
        # if the method is post then get POST data and we use instance we are 
        # seeing that we want to polpulate the form with tne original instance
        # of the user profile.
	form = UserProfileForm(request.POST, instance=request.user.profile)
	if form.is_valid():
	    form.save()
	    return HttpResponseRedirect('/accounts/loggedin')
	
    else:
        user = request.user
	# we are triggering the code 
        # User.profile = property(
        #     lambda u: UserProfile.objects.get_or_create(user = u)[0])
	profile = user.profile
	# we want to prepopulate the existing data
	form = UserProfileForm(instance=profile)
		
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('profile.html',args)


