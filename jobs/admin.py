from django.contrib import admin
from jobs.models import Job
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


admin.site.register(Job, JobAdmin)

