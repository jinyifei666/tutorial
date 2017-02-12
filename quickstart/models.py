from django.db import models
from tagging.fields import TagField
from tagging.models import Tag
from django.contrib.auth.models import User, Group

# Create your models here.
from tutorial import settings


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    tags=TagField()

    def get_tags(self):
        return Tag.objects.get_for_object(self)


    def update_tags(self, tag_names):
        Tag.objects.update_tags(self, tag_names)


    def remove_all_tags(self):
        Tag.objects.update_tags(self, None)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=30)

    address = models.CharField(max_length=50)

    city = models.CharField(max_length=60)

    state_province = models.CharField(max_length=30)

    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

  #  website = models.URLField()

class Author(models.Model):
    salutation = models.CharField(max_length=10,blank=True)

    first_name = models.CharField(max_length=30)

    last_name = models.CharField(max_length=40)

    photo = models.ImageField(verbose_name='作者照片', upload_to='image/'+"%Y"+"%m"+"%d", blank=True, null=True)

    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + str(self.last_name)

class AuthorDetail(models.Model):
    author=models.OneToOneField(Author)
    sex=models.IntegerField()
    address=models.CharField(max_length=100)



  #  headshot = models.ImageField(upload_to='/tmp',blank=True)

class FileUploader(models.Model):
    file = models.FileField(verbose_name='文件名', upload_to='file/'+"%Y"+"%m"+"%d", blank=False, null=False)
    name = models.CharField(max_length=100)  # name is filename without extension
    version = models.IntegerField(default=0)
    upload_date = models.DateTimeField(auto_now=True, db_index=True)
    owner = models.ForeignKey('auth.User', related_name='uploaded_files')
    size = models.IntegerField(default=0)

class Book(models.Model):
    # book_id = models.IntegerField()

    title = models.CharField(verbose_name='书名',max_length=100)

    authors = models.ManyToManyField(Author,verbose_name='作者')

    publisher = models.ForeignKey(Publisher,verbose_name='出版商')

    upload_datetime = models.DateTimeField(verbose_name='上传时间', blank=False, null=False, auto_now_add=True,editable=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-upload_datetime']  # 查询数据库时按时间降序排列




   # publication_date = models.DateField()

class Location(models.Model):
    time=models.CharField(verbose_name='时间',max_length=50,blank=True)
    localType=models.CharField(verbose_name='定位类型',max_length=10,blank=True)
    localTypedescription=models.CharField(verbose_name='定位类型说明',max_length=50,blank=True)
    latitude=models.CharField(verbose_name='纬度',max_length=30,blank=True)
    lontitude=models.CharField(verbose_name='经度',max_length=30,blank=True)
    radius=models.CharField(verbose_name='半径',max_length=15,blank=True)
    addr=models.CharField("地址信息",max_length=100,blank=True)
    IndoorState=models.CharField("室内状态",max_length=10,blank=True)
    locationdescribe=models.CharField("位置描述",max_length=100,blank=True)
    pointInfo=models.CharField("信息点",max_length=200,blank=True)
    locationUrl=models.CharField("位置链接",max_length=200,blank=True)

    def __str__(self):
        return self.addr

    class Meta:
        ordering = ['-time']  # 查询数据库时按时间降序排列
        verbose_name = '地址'
        verbose_name_plural = '地址'  # 不加这个会在后台显示温度后面加个s

class Temperature(models.Model):
    #我们假设体温单位都是摄氏度
    temperature = models.FloatField(verbose_name='温度数据数据', blank=False, null=False)
    measure_datetime = models.DateTimeField(verbose_name='测量时间', blank=False, null=False)
    upload_datetime = models.DateTimeField(verbose_name='上传时间', blank=False, null=False, auto_now_add=True, editable=False)
    demoInfo = models.CharField(verbose_name='其它信息', default='', blank=True, null=False, max_length=128)
    def __str__(self):
       # return self.user.nickname + '//' + str(self.temperature)
       return str(self.temperature)
    class Meta:
        verbose_name = '温度'
        verbose_name_plural = '温度'#不加这个会在后台显示温度后面加个s
        ordering=['-measure_datetime']#查询数据库时按时间降序排列
