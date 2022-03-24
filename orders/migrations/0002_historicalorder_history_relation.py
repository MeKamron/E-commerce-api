# Generated by Django 4.0.3 on 2022-03-24 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorder',
            name='history_relation',
            field=models.ForeignKey(db_constraint=False, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='records', to='orders.order'),
            preserve_default=False,
        ),
    ]