"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from rest_framework import routers
from quickstart import views
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView

from tutorial import settings

router = routers.DefaultRouter()
router.register(r'authordetail', views.AuthorDetailViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'snippet',views.SnippetViewSet)
router.register(r'temperature',views.TempertureViewSet)
router.register(r'author',views.AuthorViewSet)
router.register(r'book',views.BookViewSet)
router.register(r'publisher',views.PulisherViewSet)
router.register(r'file',views.FileUploaderViewSet)
router.register(r'location',views.LocationViewSet)

# 使用URL路由来管理我们的API
# 另外添加登录相关的URL
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
   # url(r'^',views.index),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   # url(r'^$',TemplateView,{ 'template': 'index.html' }, 'index'),
    url(r'^$',views.index,name="index"),
    url(r'^push$',views.push,name="push"),
    url(r'^location$',views.location,name="location"),
    url(r'^ceshiForm$', views.TestForm, name="ceshiForm"),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    #url(r'^accounts/', include('registration.backends.simple.urls')),
   #  url(r'^allaccounts/', include('allauth.urls')),
   #  url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
   #  url(r'^so/', include('social.apps.django_app.urls', namespace='social')),
   #  url(r'^rest-auth/', include('rest_auth.urls')),
   #  url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
   #  url(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='Twitter_login'),
   url(r'^captcha/', include('captcha.urls')),
   url(r'^hanpin/',views.hanpin),
   url(r'^disksearch/', views.disksearch)
]

urlpatterns += staticfiles_urlpatterns()#静态文件
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
