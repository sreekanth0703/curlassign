"""samproj URL Configuration

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
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from assignment import views

users_list = views.UserViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'usersmapping', views.UserMappingViewSet)

api_urls = [
    path(r'status/', views.status.as_view()),
    path(r'user_login/', views.user_login.as_view()),
    path(r'user_logout/', views.user_logout.as_view()),
    path(r'loginrequest/', views.LoginRequestView.as_view()),
    path(r'requeststatus/', views.RequestStatus.as_view()),
]

urlpatterns = [
    path(r'api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
]
