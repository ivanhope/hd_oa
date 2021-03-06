# Generated by Django 3.2.7 on 2021-09-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20210909_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='info',
            field=models.TextField(blank=True, max_length=1024, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='table',
            name='is_use',
            field=models.CharField(blank=True, choices=[('是', '是'), ('否', '否')], max_length=2, null=True, verbose_name='使用情况'),
        ),
    ]
