from django.conf.urls import include, url
from django.contrib import admin
from Dress import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dress/', include('Dress.urls')),
    url(r'^now$', views.get_now),
]
