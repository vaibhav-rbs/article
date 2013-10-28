from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()

from django_test.forms import ContactForm1, ContactForm2, ContactForm3 
from django_test.views import ContactWizard

urlpatterns = patterns('',
    (r'^articles/',include('article.urls')),
    (r'^accounts/', include('userprofile.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # user auth urls
    url(r'^accounts/login/$','django_test.views.login'),
    # url(r'^vaibhav/login/$','django_test.views.login'),
    url(r'^accounts/auth/$','django_test.views.auth_view'),
    # """do not name your view as auth as this will clash with Django's arch."""
    url(r'^accounts/logout/$','django_test.views.logout'),
    url(r'^accounts/loggedin/$','django_test.views.loggedin'),
    url(r'^accounts/invalid/$','django_test.views.invalid_login'),
    url(r'^accounts/register/$','django_test.views.register_user'),
    url(r'^accounts/register_success/$','django_test.views.register_success'),
    url(r'^contact/$',ContactWizard.as_view(
        [ContactForm1,ContactForm2,ContactForm3])
    ),
    
)
