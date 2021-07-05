
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from first_app import views

urlpatterns = [
    url(r'^$',views.help,name='index'),
    url(r'^help/',include('appTwo.urls')),
    url(r'^admin/', admin.site.urls),
]