import os

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import Snippet,Temperature,Author,Book,Publisher,FileUploader,AuthorDetail,Location
from rest_framework import permissions

class UserSerializer(serializers.HyperlinkedModelSerializer):
    permission_classes = (permissions.IsAdminUser,)
    class Meta:
        model = User
        fields = ('id','last_login','is_superuser','url','is_staff','is_active','date_joined', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        permission_classes = (permissions.IsAdminUser,)
        model = Group
        fields = ('id','url', 'name')

class LocationSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Location
        fields=("id","time","localType","localTypedescription","latitude","lontitude","radius","addr","IndoorState","locationdescribe","pointInfo","locationUrl")


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id','salutation', 'first_name',"last_name","email","photo")

class AuthorDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=AuthorDetail
        fields=("author","sex","address")

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='authors.first_name',)
    class Meta:
        permission_classes = (permissions.AllowAny,)
        model = Book
        fields = ("id",'title','author_name', 'authors',"publisher","upload_datetime")

class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id','name', "address", "city", "state_province", "country")


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Snippet
        fields=('id','created','title','code','linenos','tags')

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Temperature
        fields=('id','temperature','measure_datetime','upload_datetime','demoInfo')

class FileUploaderSerializer(serializers.ModelSerializer):
    # overwrite = serializers.BooleanField()
    class Meta:
        model = FileUploader
        fields = ('id','owner','file', 'name', 'version', 'upload_date', 'size')
        read_only_fields = ('name', 'version', 'owner', 'upload_date', 'size')

    def validate(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        validated_data['name'] = os.path.splitext(validated_data['file'].name)[0]
        validated_data['size'] = validated_data['file'].size
        # other validation logic
        return validated_data

    def create(self, validated_data):
        return FileUploader.objects.create(**validated_data)

