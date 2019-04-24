# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-02 20:57
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='advisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('credit_struct', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='current',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_year', models.IntegerField(default=2018)),
                ('current_sem', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='dean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='dean_staff_office',
            fields=[
                ('staff_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=12)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_id', models.IntegerField()),
                ('dept_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('faculty_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('password', models.CharField(default='abcdefgh', max_length=12)),
                ('email_id', models.EmailField(max_length=254)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.department')),
            ],
        ),
        migrations.CreateModel(
            name='grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='hod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='portalsOpen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crp_open', models.BooleanField(default=False)),
                ('grade_update_open', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('student_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('cgpa', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('curr_registered_credits', models.IntegerField(default=0)),
                ('max_credit', models.DecimalField(decimal_places=2, default=24, max_digits=10)),
                ('total_credits', models.DecimalField(decimal_places=2, default=24, max_digits=10)),
                ('current_year', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('current_sem', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(1)])),
                ('password', models.CharField(default='abcdefgh', max_length=50)),
                ('student_email', models.CharField(default='', max_length=100)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.department')),
            ],
        ),
        migrations.CreateModel(
            name='successfull_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.student')),
            ],
        ),
        migrations.CreateModel(
            name='takes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.student')),
            ],
        ),
        migrations.CreateModel(
            name='teaches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(1)])),
                ('year', models.IntegerField()),
                ('slot', models.CharField(max_length=2)),
                ('min_cgpa_constraint', models.DecimalField(decimal_places=2, max_digits=3)),
                ('batch', models.ManyToManyField(to='studentportal.batch')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.course')),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.faculty')),
                ('prerequisite', models.ManyToManyField(blank=True, null=True, related_name='prerequisites', to='studentportal.course')),
            ],
        ),
        migrations.CreateModel(
            name='token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1)),
                ('reason', models.TextField(default=':and:')),
                ('student_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.student')),
                ('teaches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.teaches')),
            ],
        ),
        migrations.AddField(
            model_name='takes',
            name='teaches',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.teaches'),
        ),
        migrations.AddField(
            model_name='successfull_register',
            name='teaches',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.teaches'),
        ),
        migrations.AddField(
            model_name='grades',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.student'),
        ),
        migrations.AddField(
            model_name='grades',
            name='teaches',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.teaches'),
        ),
        migrations.AddField(
            model_name='dean',
            name='faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.faculty'),
        ),
        migrations.AddField(
            model_name='course',
            name='dept_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.department'),
        ),
        migrations.AddField(
            model_name='batch',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.department'),
        ),
        migrations.AddField(
            model_name='advisor',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.batch'),
        ),
        migrations.AddField(
            model_name='advisor',
            name='faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.faculty'),
        ),
        migrations.AlterUniqueTogether(
            name='token',
            unique_together=set([('student_obj', 'teaches')]),
        ),
        migrations.AlterUniqueTogether(
            name='teaches',
            unique_together=set([('faculty_id', 'course_id', 'semester', 'year', 'slot')]),
        ),
        migrations.AlterUniqueTogether(
            name='takes',
            unique_together=set([('student_obj', 'teaches')]),
        ),
        migrations.AlterUniqueTogether(
            name='successfull_register',
            unique_together=set([('student_id', 'teaches')]),
        ),
        migrations.AlterUniqueTogether(
            name='advisor',
            unique_together=set([('faculty_id', 'batch')]),
        ),
    ]
