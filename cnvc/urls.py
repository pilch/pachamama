from django.conf.urls import patterns, include, url
from reviews import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cnvc.views.home', name='home'),
    # url(r'^cnvc/', include('cnvc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/',include('reviews.urls')),
    url(r"^account/signup/$", views.SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
)
