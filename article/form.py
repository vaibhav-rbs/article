from django import forms
from models import Article,Comment

class ArticleForm(forms.ModelForm):
	
	class Meta:
		model = Article
		# include the name of the fields in the models.py to display in the 
		# meta function.
		fields = ('title','body','pub_date','thumbnail')
		
class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('name','body')
