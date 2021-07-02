urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls)
]

from django.conf.urls import url
from django.contrib import admin
from appTwo import views