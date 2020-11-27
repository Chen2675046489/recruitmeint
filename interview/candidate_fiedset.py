# 分组显示内容
default_fieldsets = (
        (None, {'fields': ("user_id", ("username", "city", "phone"), ("email", "apply_position", "born_address"),
                           ("gender", "candidate_remark"), ("bachelor_school", "master_school", "doctor_school"),
                           "major", ("degree", "test_score_of_general_ability"), "paper_score", "last_editor")}),
        ('第一轮面试记录', {'fields': ("first_score", "first_learning_ability", "first_professional_competency",
                                "first_advantage", "first_disadvantage", "first_result", "first_recommend_position",
                                "first_interviewer_user", "first_remark",)}),
        ('第二轮专业复试记录', {'fields': ("second_score", "second_learning_ability", "second_professional_competency",
                                  "second_pursue_of_excellence", "second_pressure_score", "second_advantage",
                                  "second_disadvantage", "second_result", ("second_recommend_position",
                                                                           "second_interviewer_user",
                                                                           "second_remark")
                                  ,)}),
        ('HR第三轮复试记录', {'fields': ("hr_score", ("hr_responsibility", "hr_communication_ability", "hr_logic_ability"),
                                  ("hr_potential", "hr_stability"), "hr_advantage", "hr_disadvantage", "hr_result",
                                  "hr_interviewer_user", "hr_remark",)})
    )

# 第一面面试官展示的内容
default_fieldsets_first = (
        (None, {'fields': ("user_id", ("username", "city", "phone"), ("email", "apply_position", "born_address"),
                           ("gender", "candidate_remark"), ("bachelor_school", "master_school", "doctor_school"),
                           "major", ("degree", "test_score_of_general_ability"), "paper_score", "last_editor")}),
        ('第一轮面试记录', {'fields': ("first_score", "first_learning_ability", "first_professional_competency",
                                "first_advantage", "first_disadvantage", "first_result", "first_recommend_position",
                                "first_interviewer_user", "first_remark",)}),)
# 第二面面试官展示得内容
default_fieldsets_second = (
        (None, {'fields': ("user_id", ("username", "city", "phone"), ("email", "apply_position", "born_address"),
                           ("gender", "candidate_remark"), ("bachelor_school", "master_school", "doctor_school"),
                           "major", ("degree", "test_score_of_general_ability"), "paper_score", "last_editor")}),
        ('第一轮面试记录', {'fields': ("first_score", "first_learning_ability", "first_professional_competency",
                                "first_advantage", "first_disadvantage", "first_result", "first_recommend_position",
                                "first_interviewer_user", "first_remark",)}),
        ('第二轮专业复试记录', {'fields': ("second_score", "second_learning_ability", "second_professional_competency",
                                  "second_pursue_of_excellence", "second_pressure_score", "second_advantage",
                                  "second_disadvantage", "second_result", ("second_recommend_position",
                                                                           "second_interviewer_user",
                                                                           "second_remark")
                                  ,)}),
    )

# 没有面试官编辑权限的用户
default_type = ('first_interviewer_user', 'second_interviewer_user')