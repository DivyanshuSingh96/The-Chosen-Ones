# Generated by Django 4.1.3 on 2022-11-12 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeTracker', '0007_delete_trackitem_rename_expenditure_money_expense'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='money',
            name='savings',
        ),
    ]
