# Generated by Django 4.1.3 on 2023-01-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrics_main', '0010_caregory_name_ru_caregory_name_uz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menucategory',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='menucategory',
            name='name_uz',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_ru',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_uz',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
