from django.contrib import admin
from django.db.models import Q

from interview.dingtalk import send
from interview.models import Candidate
from django.http import HttpResponse
# Register your models here.
import csv
from datetime import datetime
import logging
from interview import candidate_fiedset as cf
logger = logging.getLogger(__name__)

exportable_fields = ('username', 'city', 'phone', 'bachelor_school', 'master_school', 'doctor_school',
                     'first_result', 'first_interviewer_user', 'second_result', 'second_interviewer_user', 'hr_score',
                     'hr_result', 'hr_interviewer_user')


def notify_interviewer(modeladmin, request, queryset):
    candidates = ""
    interviewers = ""
    for obj in queryset:
        candidates = obj.username + '; ' + candidates
        interviewers = obj.first_interviewer_user.username + '; ' + interviewers
    send('候选人 %s 进入面试环节，亲爱的面试官，请准备好面试： %s' % (candidates, interviewers))


def export_model_as_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    fields_list = exportable_fields
    response['Content-Disposition'] = 'attachment; filename=exportable-list-%s.csv' \
                                      % (datetime.now().strftime('%y-%m-%d-%H-%M-%S'),
                                         )
    # 编写表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name for f in fields_list]
    )

    for obj in queryset:
        csv_line_values = []
        for field in fields_list:
            field_object = queryset.model._meta.get_field(field)
            fields_value = field_object.value_from_object(obj)
            csv_line_values.append(fields_value)
        writer.writerow(csv_line_values)
        logger.info('%s 导出 %s 条应聘者资料' % (request.user, len(queryset)))
    return response


# 可以定义函数得属性为中文名称
export_model_as_excel.short_description = '导出为CSV文件'
export_model_as_excel.allowed_permissions = ('export',)
notify_interviewer.short_description = '通知面试官面试'


# 候选人管理类
class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'creator_date', 'modified_date')

    actions = [export_model_as_excel, notify_interviewer, ]

    def has_export_permission(self, request):
        opts = self.opts
        return request.user.has_perm('%s.%s' % (opts.app_label, 'export'))

    list_display = (
        'username', 'city', 'bachelor_school', 'first_score', 'first_result', 'first_interviewer_user',
        'second_result', 'second_interviewer_user', 'hr_score', 'hr_result', 'last_editor'
    )

    # 筛选列表
    list_filter = ('city', 'first_result', 'second_result', 'hr_score', 'first_interviewer_user',
                   'second_interviewer_user', 'hr_interviewer_user')

    # 搜索内容
    search_fields = ('username', 'phone', 'email', 'bachelor_school',)

    # 排序
    ordering = ('hr_result', 'second_result', 'first_result')

    # readonly_fields = ('first_interviewer_user', 'second_interviewer_user', 'hr_interviewer_user',)

    # list_editable = ('first_interviewer_user', 'second_interviewer_user')

    # 根据当前登录的用户，判断在应聘者列表上是否有对应聘者进行面试官指定权限
    def get_list_editable(self, request):
        group_names = self.get_group_names(request.user)
        if request.user.is_superuser or 'HR' in group_names:
            return cf.default_type
        return ()

    # 使用更改函数，改变父类的方法
    def get_changelist_instance(self, request):
        self.list_editable = self.get_list_editable(request)
        return super(CandidateAdmin, self).get_changelist_instance(request)

    def get_group_names(self, user):
        group_names = []
        for g in user.groups.all():
            group_names.append(g.name)
        return group_names

    # 根据当前登录的用户，判断是否有编辑面试官的权限
    def get_readonly_fields(self, request, obj):
        group_names = self.get_group_names(request.user)
        if 'interviewer' in group_names:
            return cf.default_type
        return ()

    def get_fieldsets(self, request, obj=None):
        group_names = self.get_group_names(request.user)
        if 'interviewer' in group_names and obj.first_interviewer_user == request.user:
            return cf.default_fieldsets_first
        elif 'interviewer' in group_names and obj.second_interviewer_user == request.user:
            return cf.default_fieldsets_second
        return cf.default_fieldsets

    def get_queryset(self, request):
        qs = super(CandidateAdmin, self,).get_queryset(request)

        group_names = self.get_group_names(request.user)
        if request.user.is_superuser or 'HR' in group_names:
            return qs
        return Candidate.objects.filter(
            Q(first_interviewer_user=request.user) | Q(second_interviewer_user=request.user)
        )


admin.site.register(Candidate, CandidateAdmin)
