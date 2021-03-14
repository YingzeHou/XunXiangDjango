# Generated by Django 3.0.7 on 2021-03-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiJiPage', '0005_auto_20210102_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('technology', '科技'), ('finance', '金融'), ('consulting', '资询'), ('art', '艺术'), ('manufacture', '制造'), ('insurance', '保险'), ('health', '医疗'), ('media', '传媒'), ('education', '教育'), ('research', '科研'), ('law', '法律'), ('other', '其他')], default='technology', max_length=20),
        ),
    ]
