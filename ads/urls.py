"""ads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from property.views import PropertyView


urlpatterns = [
    url(r'^admin_ads/', admin.site.urls),
    # api
    url(r'^api/property/list/(?P<id>.*)$', PropertyView.as_view(), name='property_list'),
    url(r'^api/property/add/$', PropertyView.as_view()),
    url(r'^api/property/remove/(?P<id>[\w_-]+)$', PropertyView.as_view()),
    url(r'^api/property/edit/(?P<id>[\w_-]+)$', PropertyView.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
