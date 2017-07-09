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
from core.views import Index, Api
from property.views import PropertyView
from core import views as core_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # api
    url(r'^api/property/list/(?P<id>.*)$', PropertyView.as_view(), name='property_list'),
    url(r'^api/property/add/$', PropertyView.as_view()),
    url(r'^api/property/remove/(?P<id>[\w_-]+)$', PropertyView.as_view()),

    # webpage
    url(r'^$', Index.as_view(), name='index'),
    url(r'^api/', Api.as_view(), name='api_doc'),
    url(r'^reset/', core_views.reset, name='reset'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
