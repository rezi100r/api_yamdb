# Generated by Django 2.2.16 on 2022-04-30 14:33

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='user', help_text='укажите уровень прав', max_length=9, verbose_name='права пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.SlugField(null=True, unique=True, validators=[reviews.validators.validate_username], verbose_name='Имя пользователя'),
        ),
    ]
