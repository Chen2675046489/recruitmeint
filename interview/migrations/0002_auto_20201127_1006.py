# Generated by Django 3.1.2 on 2020-11-27 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='first_interviewer',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='hr_interviewer',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='second_interviewer',
        ),
        migrations.AddField(
            model_name='candidate',
            name='first_interviewer_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='first_interviewer_user', to=settings.AUTH_USER_MODEL,
                                    verbose_name='面试官'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='hr_interviewer_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='hr_interviewer_user', to=settings.AUTH_USER_MODEL,
                                    verbose_name='面试官'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='second_interviewer_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='second_interviewer_user', to=settings.AUTH_USER_MODEL,
                                    verbose_name='二面面试官'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='first_result',
            field=models.CharField(blank=True, choices=[('建议复试', '建议复试'), ('待定', '待定'), ('放弃', '放弃')],
                                   max_length=256, verbose_name='初试结果'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='first_score',
            field=models.DecimalField(blank=True, decimal_places=1,
                                      help_text='1-5分 极优秀；>=4.5分 优秀；4-4.4 良好；3.5-3.9 一般；3-3.4 较差；<3 差',
                                      max_digits=2, null=True, verbose_name='初始分'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_result',
            field=models.CharField(blank=True, choices=[('建议录用', '建议录用'), ('待定', '待定'), ('放弃', '放弃')],
                                   max_length=256, verbose_name='专业复试结果'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_score',
            field=models.DecimalField(blank=True, decimal_places=1,
                                      help_text='1-5分 极优秀；>=4.5分 优秀；4-4.4 良好；3.5-3.9 一般；3-3.4 较差；<3 差',
                                      max_digits=2, null=True, verbose_name='专业复试得分'),
        ),
    ]