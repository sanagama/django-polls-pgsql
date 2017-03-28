from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/polls/')), # redirect requests to '/' to 'polls/'
]

# This works too:
#
# from django.http import HttpResponseRedirect
#
# urlpatterns = [
#   url(r'^$', lambda r: HttpResponseRedirect('polls/')), # redirect requests to '/' to 'polls/'   
# ]    
#