# Generated by Django 3.0.5 on 2020-04-10 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_posttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post_type',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='my_blog.PostType'),
            preserve_default=False,
        ),
    ]
