from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
JobTypes = [
    (0, "技术类"),
    (1, "产品类"),
    (2, "运营类"),
    (3, "运维类"),
    (4, "设计类")
]

Cities = [
    (0, "北京"),
    (1, "上海"),
    (2, "广州"),
    (3, "深圳"),
    (4, "湖南"),
    (5, "福建")
]


class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位类别")
    job_name = models.CharField(max_length=120, blank=False, verbose_name="职位名称")
    job_city = models.SmallIntegerField(blank=False, choices=Cities, verbose_name="工作地点")
    job_describe = models.TextField(max_length=1024, verbose_name="职位描述")
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="职位要求")
    creator = models.ForeignKey(User, verbose_name="创建人", null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name="创建时间", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改时间", default=datetime.now)
