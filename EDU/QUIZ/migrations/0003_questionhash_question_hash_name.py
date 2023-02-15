# Generated by Django 4.1.6 on 2023-02-15 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("QUIZ", "0002_rename_prompt_question_question_text_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuestionHash",
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
                ("hash_name", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="question",
            name="hash_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="QUIZ.questionhash",
            ),
        ),
    ]
