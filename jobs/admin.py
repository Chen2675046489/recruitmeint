from django.contrib import admin, messages

from interview.models import Candidate
from jobs.models import Job, Resume
from datetime import datetime


# Register your models here.


class JobAdmin(admin.ModelAdmin):
    # 字段隐藏
    exclude = ('creator', 'created_date', "modified_date")
    # 列表显示
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')

    # 定义一个方法，让它自动调用
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)


def enter_interview_process(modeladmin, request, queryset):
    candidate_names = ""
    for resume in queryset:
        candidate = Candidate()
        candidate.__dict__.update(resume.__dict__)
        candidate.creator_date = datetime.now()
        candidate.modified_date = datetime.now()
        candidate_names = candidate.username + ',' + candidate_names
        candidate.creator = request.user.username
        candidate.save()
    messages.add_message(request, messages.INFO, '候选人：%s 已成功进入面试流程' % (candidate_names))


enter_interview_process.short_description = '进入面试流程'


class ResumeAdmin(admin.ModelAdmin):

    actions = (enter_interview_process,)

    list_display = ('username', 'applicant', 'city', 'apply_position', 'bachelor_school', 'master_school', 'major',
                    'create_date')

    readonly_fields = ('applicant', 'create_date', 'modified_date')

    fieldsets = (
        (None, {'fields': (
         'applicant', ('username', 'city', 'phone'),
         ('email', 'apply_position', 'born_address', 'gender'),
         ('bachelor_school', 'master_school'), ('major', 'degree'),
         ('create_date', 'modified_date'),
         'candidate_introduction', 'work_experience', 'project_experience')}),
    )

    # 保存为用户
    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Job, JobAdmin)
admin.site.register(Resume, ResumeAdmin)

