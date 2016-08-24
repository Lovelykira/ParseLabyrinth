from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^Aatrox/$', AatroxView.as_view()),
    url(r'^Annie/$', AnnieView.as_view()),
    url(r'^Aatrox/Evelyn/$', EvelynView.as_view()),
    url(r'^Aatrox/Malphit/$', MalphitView.as_view()),
    url(r'^Annie/Ryze/$', RyzeView.as_view()),
    url(r'^Annie/Jinx/$', JinxView.as_view()),
    url(r'^Aatrox/Evelyn/Shaco/$', ShacoView.as_view()),
    url(r'^Aatrox/Evelyn/Tristana/$', TristanaView.as_view()),
    url(r'^Aatrox/Evelyn/Shaco/Vi/$', ViView.as_view()),
    url(r'^Annie/Ryze/Zyra/$', ZyraView.as_view()),
    url(r'^$', JinxView.as_view()),
]