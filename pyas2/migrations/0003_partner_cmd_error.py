# Generated by Django 2.2.10 on 2020-03-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyas2', '0002_auto_20190603_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='cmd_error',
            field=models.TextField(blank=True, help_text='Command executed after message fails (max_retries reached), replacements are $filename, $sender, $recevier, $messageid and any message header such as $Subject', null=True, verbose_name='Command on Message Error'),
        ),
    ]
