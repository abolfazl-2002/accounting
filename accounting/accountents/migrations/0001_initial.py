# Generated by Django 3.2.8 on 2021-11-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountryTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('group', models.CharField(choices=[('+', 'income'), ('-', 'expenditrue')], default='+', max_length=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
