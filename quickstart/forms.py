from captcha.fields import CaptchaField
from django import forms
from django.forms import ModelForm
from quickstart.models import Location

class AddForm(forms.Form):
    a = forms.IntegerField(label="数字一",initial=11)
    b = forms.IntegerField()
    captcha = CaptchaField()

class hanForm(forms.Form):
    han=forms.CharField(label="汉字")
    spilt=forms.ChoiceField(choices=(('', '无'),('-', '-')),required=False)
    cap=CaptchaField()

class LocationForm(ModelForm):
    class Meta:
        model=Location
        fields = '__all__'
    # time=forms.CharField(label="时间")
    # localType=forms.CharField(lable='定位类型')
    # localTypedescription=forms.CharField(lable='定位类型说明')
    # latitude=forms.CharField(lable='纬度')
    # lontitude=forms.CharField(lable='经度')
    # radius=forms.CharField(lable='半径')
    # addr=forms.CharField(lable="地址信息")
    # IndoorState=forms.CharField(lable="室内状态")
    # locationdescribe=forms.CharField(lable="位置描述")<textarea></textarea>


class diskForm(forms.Form):
    key=forms.CharField(label="关键字")
