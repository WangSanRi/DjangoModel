from django.core.exceptions import ValidationError
from app01 import models
from django import forms
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.encrypt import md5

class UserModelForm(BootStrapModelForm):
    name = forms.CharField(min_length=3,label="用户名")
    class Meta:
        model = models.UserInfo
        fields = "__all__"

class PrettyModelForm(BootStrapModelForm):
    # 验证方式1
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')],
    # )
    class Meta:
        model = models.PrettyNum
        fields = "__all__"
    # 验证方式2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return txt_mobile

class PrettyEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.PrettyNum
        fields = ['mobile','price','level','status']
    # 验证方式2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return txt_mobile

class AdminModelForm(BootStrapModelForm):
    confirm = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )
    class Meta:
        model = models.Admin
        fields = "__all__"
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm(self):
        pwd = self.cleaned_data.get("password")
        confirm_pwd = md5(self.cleaned_data.get("confirm"))
        if confirm_pwd != pwd:
            raise ValidationError("密码不一致")
        return confirm_pwd

class AdminResetModelForm(BootStrapModelForm):
    confirm = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )
    class Meta:
        model = models.Admin
        fields = ["password","confirm"]
        widgets = {
            "password":forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)
        exists = models.Admin.objects.filter(id=self.instance.pk,password=md5_pwd).exists()
        if exists:
            raise ValidationError("新密码与原密码不能相同")
        return md5_pwd

    def clean_confirm(self):
        pwd = self.cleaned_data.get("password")
        confirm_pwd = md5(self.cleaned_data.get("confirm"))
        if confirm_pwd != pwd:
            raise ValidationError("密码不一致")
        return confirm_pwd

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", widget=forms.TextInput, required=True)
    password = forms.CharField(label="密码", widget=forms.PasswordInput(render_value=True), required=True)
    code = forms.CharField(label="验证码", widget=forms.TextInput, required=True)
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {"class":"form-control"}
                field.widget.attrs["placeholder"] = field.label
