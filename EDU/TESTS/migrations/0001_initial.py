# Generated by Django 4.1.5 on 2023-01-25 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("test_question", models.CharField(blank=True, max_length=100000)),
                ("test_answer", models.CharField(blank=True, max_length=100000)),
                (
                    "course_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="TESTS.course"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="subject_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="TESTS.subject"
            ),
        ),
    ]
