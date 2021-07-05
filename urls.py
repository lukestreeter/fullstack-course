from django.conf.urls import url,include
from first_app import views
from first_app import views

urlpatterns = [
    url(r'^$',views.index,name=index)
    url(r'^admin/', admin.site.urls),
    url(r'first_app/',include('first_app.urls'))
]