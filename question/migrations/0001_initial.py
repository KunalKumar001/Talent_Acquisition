# Generated by Django 3.0.2 on 2020-03-17 05:46

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('typ', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('option', jsonfield.fields.JSONField(default=dict)),
                ('answer', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('option_available', models.BooleanField(default=False)),
                ('questionstyp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='typ.QuestionType')),
            ],
            options={
                'db_table': 'questions',
            },
        ),
    ]
