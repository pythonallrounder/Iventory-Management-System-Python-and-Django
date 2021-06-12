# Generated by Django 3.0.2 on 2020-02-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('Avialable', 'Ready to Purchase'), ('Sold', 'Item Sold'), ('Restockin', 'Item Restocking in few days')], default='sold', max_length=10)),
                ('issue', models.CharField(default='No isssue', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('Avialable', 'Ready to Purchase'), ('Sold', 'Item Sold'), ('Restockin', 'Item Restocking in few days')], default='sold', max_length=10)),
                ('issue', models.CharField(default='No isssue', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('Avialable', 'Ready to Purchase'), ('Sold', 'Item Sold'), ('Restockin', 'Item Restocking in few days')], default='sold', max_length=10)),
                ('issue', models.CharField(default='No isssue', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]