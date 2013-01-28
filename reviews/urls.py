from django.conf.urls import patterns, url

from reviews import views

urlpatterns = patterns('',
    url(r'^$',views.register,name='register')
)