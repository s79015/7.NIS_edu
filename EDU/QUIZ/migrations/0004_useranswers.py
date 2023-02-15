# Generated by Django 4.1.6 on 2023-02-15 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("QUIZ", "0003_questionhash_question_hash_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserAnswers",
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
                ("user_name", models.CharField(max_length=100)),
                ("quiz_name", models.CharField(max_length=100)),
                (
                    "quiz_hash_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "question_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("user_answer_is_correct", models.BooleanField()),
                ("user_spend_time", models.IntegerField(blank=True, null=True)),
                (
                    "answer_date",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 2, 15, 16, 7, 33, 146598)
                    ),
                ),
            ],
        ),
    ]
