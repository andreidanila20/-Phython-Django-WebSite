# Generated by Django 3.1.3 on 2020-12-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201209_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Ceva', max_length=100)),
                ('first_name', models.CharField(default='Ceva', max_length=100)),
                ('last_name', models.CharField(default='Ceva', max_length=100)),
                ('email', models.CharField(default='Ceva', max_length=100)),
            ],
        ),
    ]
