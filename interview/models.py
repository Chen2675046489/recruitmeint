from django.contrib.auth.models import User
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
    first_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name="初始分",
                                      help_text='1-5分 极优秀；>=4.5分 优秀；4-4.4 良好；3.5-3.9 一般；3-3.4 较差；<3 差')
    first_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                 verbose_name="学习能力得分")
    first_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=2,
                                                        verbose_name="专业能力得分")

    first_advantage = models.TextField(max_length=1024, blank=True, verbose_name='优势')
    first_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name='顾虑和不足')
    first_result = models.CharField(max_length=256, choices=FIRST_INTERVIEW_RESULT_TYPE, blank=True,
                                    verbose_name='初试结果')
    first_recommend_position = models.CharField(max_length=256, blank=True, verbose_name='推荐部分')
    first_interviewer_user = models.ForeignKey(User, related_name='first_interviewer_user', blank=True, null=True,
                                               on_delete=models.CASCADE, verbose_name='面试官')
    first_remark = models.CharField(max_length=256, blank=True, verbose_name='初试备注')

    # 第二轮面试
    second_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name='专业复试得分',
                                       help_text='1-5分 极优秀；>=4.5分 优秀；4-4.4 良好；3.5-3.9 一般；3-3.4 较差；<3 差')
    second_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                  verbose_name='学习能力得分')
    second_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                         verbose_name='追求卓越得分')
    second_pursue_of_excellence = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                      verbose_name='沟通能力得分')
    second_pressure_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                verbose_name='抗压能力得分')
    second_advantage = models.TextField(max_length=1024, blank=True, verbose_name='优势')
    second_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name='顾虑和不足')
    second_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True,
                                     verbose_name='专业复试结果')
    second_recommend_position = models.CharField(max_length=256, blank=True, verbose_name='建议方向或推荐部门')
    second_interviewer_user = models.ForeignKey(User, related_name='second_interviewer_user', blank=True, null=True,
                                                on_delete=models.CASCADE, verbose_name='二面面试官')
    second_remark = models.CharField(max_length=256, blank=True, verbose_name='专业复试备注')

    # HR终面
    hr_score = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR复试综合等级')
    hr_responsibility = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR责任心')
    hr_communication_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                                verbose_name='坦诚沟通')
    hr_logic_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR逻辑思维')
    hr_potential = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR发展能力')
    hr_stability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR稳定性')
    hr_advantage = models.TextField(max_length=1024, blank=True, verbose_name='优势')
    hr_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name='顾虑与不足')
    hr_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name='HR复试结果')
    hr_interviewer_user = models.ForeignKey(User, related_name='hr_interviewer_user', blank=True, null=True,
                                            on_delete=models.CASCADE, verbose_name='面试官')
    hr_remark = models.CharField(max_length=256, blank=True, verbose_name='HR面试备注')

    creator = models.CharField(max_length=256, blank=True, verbose_name='候选人数据的创建人')
    creator_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新时间')
    last_editor = models.CharField(max_length=256, blank=True, verbose_name='最后编辑人')

    class Meta:
        db_table = 'candidate'
        verbose_name = '应聘者'
        verbose_name_plural = '应聘者'

        permissions = [
            ('export', 'Can export candidate list'),
            ("notify", "notify interviewer for candidate review"),
        ]

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username
