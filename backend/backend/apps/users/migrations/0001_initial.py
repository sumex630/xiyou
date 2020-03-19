# Generated by Django 2.1.8 on 2020-03-19 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subs', to='users.Area', verbose_name='上级行政区划')),
            ],
            options={
                'verbose_name': '行政区划',
                'verbose_name_plural': '行政区划',
                'db_table': 'tb_areas',
            },
        ),
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('url', models.CharField(max_length=300, null=True, verbose_name='详情链接')),
                ('content', models.TextField(blank=True, null=True, verbose_name='人员详情')),
                ('brief_intro', models.TextField(blank=True, null=True, verbose_name='人员简介')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='人员邮箱')),
                ('views', models.CharField(max_length=20, null=True, verbose_name='浏览数')),
                ('code', models.CharField(max_length=20, verbose_name='人员编码')),
                ('sex', models.CharField(max_length=20, null=True, verbose_name='性別')),
                ('main_fields', models.CharField(max_length=20, null=True, verbose_name='人员编码')),
                ('areas', models.ManyToManyField(db_table='tb_collect', to='users.Area', verbose_name='专业和人员关联表')),
            ],
            options={
                'verbose_name': '人员信息',
                'verbose_name_plural': '人员信息',
                'db_table': 'tb_person',
            },
        ),
    ]
