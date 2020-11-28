from django.conf.urls import url
from django.urls import path

from jobs import views

urlpatterns = [
    url(r'^joblist/', views.joblist, name="joblist"),
    url(r"^job/(?P<job_id>\d+)/$", views.detail, name="detail"),
    path(r'resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),
    path(r'resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),

    # 首页自动跳转到 职位列表
    url(r"^$", views.joblist, name="name")

]
