# Generated by Django 3.0.3 on 2020-05-30 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameofSchool', models.CharField(max_length=256)),
                ('nameofPrincipal', models.CharField(max_length=256)),
                ('locationofSchool', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='studentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameofStudent', models.CharField(max_length=256)),
                ('ageofStuden', models.PositiveIntegerField()),
                ('nameofSchool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='django_first_app.School')),
            ],
        ),
    ]
