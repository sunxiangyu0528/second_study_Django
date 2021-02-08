# Generated by Django 3.1.6 on 2021-02-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='项目名称', max_length=200, unique=True, verbose_name='项目名称')),
                ('leader', models.CharField(help_text='负责人', max_length=200, verbose_name='负责人')),
                ('tester', models.CharField(help_text='测试人员', max_length=200, verbose_name='测试人员')),
                ('publish_app', models.CharField(help_text='发布应用', max_length=200, verbose_name='发布应用')),
                ('programer', models.CharField(help_text='开发人员', max_length=200, verbose_name='开发人员')),
                ('desc', models.TextField(blank=True, default='', help_text='简要描述', null=True, verbose_name='简要描述')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
                'db_table': 'tb_projects',
            },
        ),
    ]
