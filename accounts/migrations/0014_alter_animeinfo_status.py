# Generated by Django 4.1.1 on 2022-10-05 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_customer_profile_pic_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animeinfo',
            name='status',
            field=models.CharField(choices=[('Still Airing', 'Still Airing'), ('Completed', 'Completed')], default=None, max_length=20, null=True),
        ),
    ]
