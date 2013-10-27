from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	# This class will define what fields will be dispalyed in the webapage. 
    email = forms.EmailField(required = True)
    
    class Meta:
    #to hold anything which is not in field meta data for actual class, way to tell Django about what the model is and what field its going to 
    #contain
        model = User
        fields = ('username','email','password1','password2')
    
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        
        return user
    
    
# we will demostrate how to carry information among difffrent pages

class ContactForm1(forms.Form):
	subject = forms.CharField(max_length = 100)
	    
	  
class ContactForm2(forms.Form):
	sender = forms.EmailField()
	
class ContactForm3(forms.Form):
	message = forms.CharField(widget = forms.Textarea)
	

