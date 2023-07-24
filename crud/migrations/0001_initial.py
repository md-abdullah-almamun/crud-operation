# Generated by Django 4.2.2 on 2023-07-23 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=25, null=True)),
                ('Image', models.ImageField(blank=True, default='default/def.jpg', null=True, upload_to='Profile_pic/')),
                ('Email', models.EmailField(blank=True, max_length=20, null=True)),
                ('Age', models.PositiveIntegerField(blank=True, null=True)),
                ('Address', models.TextField(blank=True, max_length=200, null=True)),
                ('Phone_no', models.TextField(blank=True, max_length=15, null=True)),
                ('Date_of_birth', models.TextField(blank=True, max_length=12, null=True)),
                ('Religion', models.CharField(choices=[('Muslim', 'Muslim'), ('Hindu', 'Hindu'), ('Christian', 'Christian'), ('Bouddho', 'Bouddho')], max_length=9)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'others')], max_length=6)),
            ],
        ),
    ]