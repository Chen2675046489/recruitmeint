from django.contrib import admin
from interview.models import Candidate
# Register your models here.


class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'creator_date', 'modified_date')

    list_display = (
        'username', 'city', 'bachelor_school', 'first_score', 'first_result', 'first_interviewer',
        'second_result', 'second_interviewer', 'hr_score', 'hr_result', 'last_editor'
    )
    fieldsets = (
        (None, {'fields': ("userid", "username",)}),
        ('第一轮面试记录', {'fields': ("",)}),
        ('第二轮面试记录', {'fields': ("",)}),
        ('HR终面记录', {'fields': ("",)}),
    )

admin.site.register(Candidate, CandidateAdmin)
