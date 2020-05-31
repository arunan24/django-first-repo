"""django_third_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django_first_app import views


from django.urls import path

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    url(r'^CBVView',views.ClassBasedBiewname.as_view(),name="cbvview"),
    url(r'^CBVTView', views.CBVTemapleView.as_view(), name="cbvtview"),
    url(r'^School',views.schoolListView.as_view(),name="school"),
    url(r'^(?P<pk>[-\w])/$',views.studentDetailView.as_view(),name="student"),
    url(r'^Create/$',views.createschool.as_view(),name="create"),
    url(r'^Update/(?P<pk>[-\w])/$',views.updateschool.as_view(),name="update"),
    url(r'^Delete/(?P<pk>[-\w])/$',views.deleteschool.as_view(),name="delete"),


]
