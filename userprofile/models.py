from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	# we are tying relationship b/w Userprofile and user by onetoone fields
	# one user --> one UserProfile
	# one UserProfile --> one user
	# --> related to  
	user = models.OneToOneField(User)
	likes_cheese =  models.BooleanField()
	favourite_hamster_name =  models.CharField(max_length = 50)
	
# defining a property which should do pass a user objects to this property and this models and this will fire off this get_or_create method and if it does 
# not have one then User profile is created however if it already have one then it returns the new one  
User.profile = property(lambda u: UserProfile.objects.get_or_create(user = u)[0])
