# Generated by Django 2.0.4 on 2018-04-08 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('types', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactioncategory',
            options={'verbose_name_plural': 'Transaction categories'},
        ),
        migrations.AddField(
            model_name='budget',
            name='end_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='start_date',
            field=models.DateField(default=None, null=True),
        ),
    ]