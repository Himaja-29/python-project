# Generated by Django 5.0 on 2024-02-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0003_alter_sharu_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbackform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('feedback_message', models.TextField()),
            ],
            options={
                'db_table': 'Feedbackform',
            },
        ),
        migrations.DeleteModel(
            name='sharu',
        ),
    ]
