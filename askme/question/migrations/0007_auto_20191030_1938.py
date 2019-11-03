# Generated by Django 2.2.6 on 2019-10-30 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0006_auto_20191030_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authors', to='question.Profile'),
        ),
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(to='question.Profile', verbose_name='Лайки'),
        ),
    ]