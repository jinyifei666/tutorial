import datetime
import json
import logging
import os
import uuid
from urllib.request import Request, urlopen

import django_filters
from PIL import ImageFile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import jpush
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from jpush import common
from django.shortcuts import render, render_to_response

# Create your views here.
from django.contrib.auth.models import User, Group
# from rest_auth.views import LoginView
from django.template import RequestContext
from rest_framework import viewsets,generics,mixins
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponseRedirect
from rest_framework.parsers import FormParser, FileUploadParser,MultiPartParser
from quickstart.models import Snippet,Temperature,Author,Book,Publisher,FileUploader,AuthorDetail,Location
from quickstart.serializers import UserSerializer, GroupSerializer,SnippetSerializer,TemperatureSerializer,LocationSeralizer,PublisherSerializer,AuthorSerializer,BookSerializer,FileUploaderSerializer,AuthorDetailSerializer
from tutorial import settings
# from rest_auth.registration.views import SocialLoginView
# from rest_auth.social_serializers import *
# from allauth.socialaccount.providers.weixin.views import WeixinOAuth2Adapter
from tutorial.settings import *
from quickstart.forms import AddForm,hanForm, diskForm,LocationForm
from xpinyin import Pinyin


class UserViewSet(viewsets.ModelViewSet):
    """
    查看、编辑用户的界面
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
#    parser_classes = (FormParser, MultiPartParser, )
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username','id',)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSeralizer






class GroupViewSet(viewsets.ModelViewSet):
    """
    查看、编辑组的界面
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class TempertureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class =BookSerializer

class AuthorDetailViewSet(viewsets.ModelViewSet):
    queryset = AuthorDetail.objects.all()
    serializer_class = AuthorDetailSerializer

class PulisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer



class FileUploaderViewSet(viewsets.ModelViewSet):
    serializer_class = FileUploaderSerializer
    parser_classes = (MultiPartParser, FormParser,)

    # overriding default query set
    queryset = FileUploader.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = super(FileUploaderViewSet, self).get_queryset(*args, **kwargs)
        qs = qs.filter(owner=self.request.user)
        return qs


def index(request):
     return HttpResponseRedirect('/accounts/login/')

def push(request):
    if request.method == 'POST':
        type = request.POST["type"]
        title = request.POST["title"]
        content = request.POST["content"]
        _jpush = jpush.JPush(app_key, master_secret)
        push = _jpush.create_push()
        _jpush.set_logging("DEBUG")
        push.audience = jpush.all_
        if type=="1":
            push.notification = jpush.notification(alert=title + content)
        elif type=='2':
            push.message = jpush.message(msg_content=title + content,extras="sss")
        push.platform = jpush.all_
        try:
            response = push.send()
        except common.Unauthorized:
            raise common.Unauthorized("Unauthorized")
        except common.APIConnectionException:
            raise common.APIConnectionException("conn")
        except common.JPushFailure:
            print("JPushFailure")
        except:
            print("Exception")
        logging.debug("past"+title+content)
        c = {"title": "标题", "content": "内容"}
        return render(request, "push.html", c)
    c={"title":"标题","content":"内容"}
    return render(request,"push.html",c)


def TestForm(request):
    if request.method == 'POST':  # 当提交表单时

        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'ceshiForm.html', {'form': form})

def hanpin(request):
    if request.method=='POST':
        form = hanForm(request.POST)
        if form.is_valid():
            hanzi=form.cleaned_data["han"]
            spilt=form.cleaned_data['spilt']
            p=Pinyin()
            return HttpResponse(p.get_pinyin(hanzi,spilt))
    else:
        form=hanForm()
    return render(request,"hanpin.html",{'form':form})

def disksearch(request):
    if request.method=='POST':
        form=diskForm(request.POST)
        if form.is_valid():
            host = 'http://netdisk.market.alicloudapi.com'
            path = '/search'
            method = 'GET'
            appcode = '43c904e20cea4ac38a882bef8d450357'
            querys = 'page=1&q='+form.cleaned_data['key']
            bodys = {}
            url = host + path + '?' + querys

            request =Request(url)
            request.add_header('Authorization', 'APPCODE ' + appcode)
            response = urlopen(request)
            content = response.read()
            return JsonResponse(content)
    else:
        form = diskForm()
    return render(request, "disksearch.html", {'form': form})


@csrf_exempt
def location(request):
    if request.method=='POST':
        form=LocationForm(request.POST)
        if form.is_valid():
            # #form.cleaned_data["locationUrl"]="http://api.map.baidu.com/marker?location="+form.cleaned_data["latitude"]+","+form.cleaned_data["lontitude"]+"&title=位置(金义飞提供)&content="+form.cleaned_data["locationdescribe"]+"&output=html"
            # form.locationUrl="http://api.map.baidu.com/marker?location="+form.cleaned_data["latitude"]+","+form.cleaned_data["lontitude"]+"&title=位置(金义飞提供)&content="+form.cleaned_data["locationdescribe"]+"&output=html"
            # print(form)
            # print(form.cleaned_data["locationUrl"])
            # #print(form)
            temp1=form.save()  #form类行转变为model类型
            temp1.locationUrl = "http://api.map.baidu.com/marker?location=" + form.cleaned_data["latitude"] + "," + form.cleaned_data["lontitude"] + "&title=位置(金义飞提供)&content=" + form.cleaned_data["locationdescribe"] + "&output=html"
            temp1.save()
            return JsonResponse({"state":1,"url":temp1.locationUrl})
        else:
            return JsonResponse({"state": 0})
    else:
        form=LocationForm
        return render(request,"location.html",{"form":form})


