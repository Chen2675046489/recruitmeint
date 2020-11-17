from django.db import models

# Create your models here.
# 第一轮面试结果
FIRST_INTERVIEW_RESULT_TYPE = ((u"建议复试", u"建议复试"), (u"待定", u"待定"), (u"放弃", u"放弃"))
# 第二轮面试结果
INTERVIEW_RESULT_TYPE = ((u"建议录用", u"建议录用"), (u"待定", u"待定"), (u"放弃", u"放弃"))
# 候选人学历
DEGREE_TYPE = ((u"本科", u"本科"), (u"硕士", u"硕士"), (u"博士", u"博士"))
# 面试结果
HR_SCORE_TYPE = (("S", "S"), ("A", "A"), ("B", "B"), ("C", "C"))


class Candidate(models.Model):
    user_id = models.IntegerField(unique=True, blank=True, null=True, verbose_name="应聘者ID")
    username = models.CharField(max_length=155, verbose_name="应聘者名称")
    city = models.CharField(max_length=155, verbose_name="城市")
    phone = models.CharField(max_length=135, verbose_name="手机号")
    email = models.EmailField(max_length=135, verbose_name="邮箱")
    apply_position = models.CharField(max_length=135, blank=True, verbose_name="应聘职位")
    born_address = models.CharField(max_length=135, blank=True, verbose_name="户籍")
    gender = models.CharField(max_length=135, blank=True, verbose_name="性别")
    candidate_remark = models.CharField(max_length=255, blank=True, verbose_name="备注")

    # 学校和学历
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name="本科学校")
    master_school = models.CharField(max_length=135, blank=True, verbose_name="研究生学校")
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name="博士生学校")
    major = models.CharField(max_length=135, blank=True, verbose_name="专业")
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name="学历")

    # 综合能力测评成绩，笔试测评成绩
    test_score_of_general_ability = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True,
                                                        verbose_name="综合能力测评成绩")
    paper_score = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True, verbose_name="笔试成绩")

    # 第一轮面试结果
    first_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name="初始分数")
    first_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                 verbose_name="学习能力得分")
    first_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=2,
                                                        verbose_name="专业能力得分")

