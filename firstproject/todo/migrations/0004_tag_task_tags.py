# Generated by Django 4.2.6 on 2023-10-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0003_alter_task_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(related_name="tasks", to="todo.tag"),
        ),
    ]