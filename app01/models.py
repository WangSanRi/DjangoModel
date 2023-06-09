from django.db import models

class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name='名称',max_length=32)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name='姓名',max_length=116)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2,default=0)
    create_time = models.DateField(verbose_name='入职时间')
    sex_choices = ((1,"男"),(2,"女"))
    sex = models.SmallIntegerField(verbose_name='性别',choices=sex_choices)
    depart = models.ForeignKey(to="Department",to_field="id",on_delete=models.CASCADE)

class PrettyNum(models.Model):
    """靓号表"""
    mobile = models.CharField(verbose_name="手机号",max_length=11)
    price = models.IntegerField(verbose_name="价格")
    level_choices = ((1,"1级"),(2,"2级"),(3,"3级"),(4,"4级"))
    level = models.SmallIntegerField(verbose_name="级别",choices=level_choices,default=1)
    status_choices = ((1, "已占用"), (2, "未占用"))
    status = models.SmallIntegerField(verbose_name="状态",choices=status_choices,default=2)

class Admin(models.Model):
    """ 管理员 """
    username = models.CharField(verbose_name="用户名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)

