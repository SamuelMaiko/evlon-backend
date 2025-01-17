# Generated by Django 5.0.2 on 2024-04-03 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evlon', '0003_alter_post_imageurl_alter_post_smallprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Attendance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='commentsCount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='counter',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='likesCount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='smallProfile',
            field=models.CharField(blank=True, default='./Rong.jpg', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeRemaining',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
