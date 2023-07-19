# Generated by Django 3.2.4 on 2023-07-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("encrypt", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="rsakey",
            options={"verbose_name": "非对称加密密钥", "verbose_name_plural": "非对称加密密钥"},
        ),
        migrations.AddField(
            model_name="rsakey",
            name="cipher_type",
            field=models.CharField(default="RSA", max_length=64, verbose_name="加密类型"),
        ),
        migrations.AlterUniqueTogether(
            name="rsakey",
            unique_together={("name", "type", "cipher_type")},
        ),
    ]