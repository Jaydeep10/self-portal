from django.conf.urls import url,include
from django.contrib import admin
from potfoli import views

app_name = 'potfoli'


urlpatterns = [
    url(r'^$', views.Welcome.as_view(), name = 'home'),
    url(r'^resume/', views.Resume.as_view(), name = 'resume'),
    url(r'^about/', views.About.as_view(), name = 'about'),
    url(r'^contact/', views.Contact.as_view(), name = 'contact'),

]
