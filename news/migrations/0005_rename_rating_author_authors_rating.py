# Generated by Django 3.2.2 on 2021-05-22 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_author_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='rating',
            new_name='authors_rating',
        ),
    ]