from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='余额', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='入职时间')
    # did = models.BigIntegerField(verbose_name='部门id')
    # dpart = models.ForeignKey(to="Department", to_fields="id", on_delete=models.CASCADE)
    dpart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    gender_choices = ((1, "男"), (2, "女"))
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)


class Department(models.Model):
    title = models.CharField(verbose_name='标题', max_length=16)
