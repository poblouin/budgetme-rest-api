# Generated by Django 2.0.4 on 2018-04-08 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('types', '0002_auto_20180408_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactioncategory',
            name='budget',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transaction_categories', to='types.Budget'),
            preserve_default=False,
        ),
    ]
