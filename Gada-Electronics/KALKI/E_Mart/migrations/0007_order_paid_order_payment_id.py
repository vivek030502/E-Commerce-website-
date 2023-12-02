# Generated by Django 4.2.7 on 2023-11-30 02:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("E_Mart", "0006_orderitem_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="paid",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="payment_id",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
