from django.conf.urls import url
from jobs import views

urlpatterns = [
    url(r'^joblist/', views.joblist, name="joblist"),
    url(r"^job/(?P<job_id>\d+)/$", views.detail, name="detail"),

    # 首页自动跳转到 职位列表
    url(r"^$", views.joblist, name="name")
]