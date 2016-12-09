"""annotation_ui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from rest_framework.routers import DefaultRouter

from annotator import views
from annotator import viewsets

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='welcome'),
    url(r'^annotate/(?P<person_id>[0-9]+)/$', views.annotate, name='annotate'),
    url(r'^drugs/next/(?P<person_id>[0-9]+)/$', views.get_next_drug),

    url(r'^partials/drugdetail/(?P<drug_id>[0-9]+)/$', views.partial_drug_detail),
    url(r'^partials/annotations/(?P<drug_id>[0-9]+)/$', views.partial_annotations),
]

# Django REST Framework
router = DefaultRouter()
router.register(r'drugs', viewsets.DrugViewSet)
router.register(r'annotations', viewsets.AnnotationViewSet)

urlpatterns += router.urls
