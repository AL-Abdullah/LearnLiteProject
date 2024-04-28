# Generated by Django 5.0.1 on 2024-04-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_remove_generatedtest_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], default='a', max_length=1),
        ),
    ]