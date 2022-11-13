# Generated by Django 4.1.3 on 2022-11-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeTracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='trackItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.FloatField(null=True)),
                ('savings', models.FloatField(null=True)),
                ('expenditure', models.FloatField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]