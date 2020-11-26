from django.contrib import admin
from interview.models import Candidate
from django.http import HttpResponse
# Register your models here.
import csv
from datetime import datetime
import logging
logger = logging.getLogger(__name__)

exportable_fields = ('username', 'city', 'phone', 'bachelor_school', 'master_school', 'doctor_school',
                     'first_result', 'first_interviewer', 'second_result', 'second_interviewer', 'hr_score', 'hr_result'
                     )


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
        logger.info('%s 导出 %s 条应聘者资料' %(request.user, len(queryset)))
    return response


# 可以定义函数得属性为中文名称
export_model_as_excel.short_description = '导出为CSV文件'


# 候选人管理类
class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'creator_date', 'modified_date')

    actions = [export_model_as_excel, ]

    list_display = (
        'username', 'city', 'bachelor_school', 'first_score', 'first_result', 'first_interviewer',
        'second_result', 'second_interviewer', 'hr_score', 'hr_result', 'last_editor'
    )

    # 筛选列表
    list_filter = ('city', 'first_result', 'second_result', 'hr_score', 'first_interviewer', 'second_interviewer',
                   'hr_interviewer')

    # 搜索内容
    search_fields = ('username', 'phone', 'email', 'bachelor_school',)

    # 排序
    ordering = ('hr_result', 'second_result', 'first_result')

    # 分组显示内容
    fieldsets = (
        (None, {'fields': ("user_id", ("username", "city", "phone"), ("email", "apply_position", "born_address"), ("gender",
                           "candidate_remark"), ("bachelor_school", "master_school", "doctor_school"), "major",
                           ("degree", "test_score_of_general_ability"), "paper_score", "last_editor")}),
        ('第一轮面试记录', {'fields': ("first_score", "first_learning_ability", "first_professional_competency",
                                "first_advantage", "first_disadvantage", "first_result", ("first_recommend_position",
                                                                                          "first_interviewer",
                                                                                          "first_remark"),)}),
        ('第二轮专业复试记录', {'fields': ("second_score", "second_learning_ability", "second_professional_competency",
                                  "second_pursue_of_excellence", "second_pressure_score", "second_advantage",
                                  "second_disadvantage", "second_result", ("second_recommend_position",
                                                                             "second_interviewer", "second_remark"),)}),
        ('HR第三轮复试记录', {'fields': ("hr_score", ("hr_responsibility", "hr_communication_ability", "hr_logic_ability"),
                                  ("hr_potential", "hr_stability"), "hr_advantage", "hr_disadvantage", "hr_result",
                                  "hr_interviewer", "hr_remark",)})
    )


admin.site.register(Candidate, CandidateAdmin)
