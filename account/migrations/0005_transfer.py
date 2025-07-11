# Generated by Django 5.2.2 on 2025-06-12 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_deposit_deposit_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('from_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='account.useraccount')),
                ('to_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='account.useraccount')),
            ],
        ),
    ]
