urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^first_app/',include('first.app.urls')),
    url(r'^admin/', admin.site.urls),
]

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from first_app import views