# Generated by Django 2.0 on 2019-06-11 11:43

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='作者姓名')),
                ('introduce_link', models.CharField(max_length=30, verbose_name='作者简介链接')),
                ('introduces', models.CharField(max_length=300, verbose_name='作者简介')),
                ('avatar_link', models.ImageField(blank=True, null=True, upload_to='daodus/avatar_imgs', verbose_name='作者头像')),
            ],
            options={
                'verbose_name': '书籍作者详情',
                'verbose_name_plural': '书籍作者详情',
                'db_table': 'GX_book_author',
            },
        ),
        migrations.CreateModel(
            name='BookDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='书名')),
                ('img_link', models.ImageField(blank=True, null=True, upload_to='daodus/book_images', verbose_name='书籍图片')),
                ('desc', models.CharField(max_length=500, verbose_name='书籍描述信息')),
                ('browse_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='浏览量')),
                ('publishing_house', models.CharField(blank=True, max_length=20, null=True, verbose_name='出版社')),
                ('publishing_date', models.DateField(blank=True, null=True, verbose_name='出版日期')),
                ('page_count', models.IntegerField(blank=True, null=True, verbose_name='页数')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='定价')),
                ('IBSN', models.CharField(blank=True, max_length=20, null=True, verbose_name='书籍IBSN号码')),
                ('catalog', DjangoUeditor.models.UEditorField(blank=True, default='', null=True, verbose_name='书籍目录')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.BookAuthor', verbose_name='作者')),
            ],
            options={
                'verbose_name': '书籍详情',
                'verbose_name_plural': '书籍详情',
                'db_table': 'GX_book_detail',
            },
        ),
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('desc', models.CharField(blank=True, max_length=300, null=True, verbose_name='类别描述信息')),
                ('book_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目')], help_text='类目级别', verbose_name='类目级别')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('parent_forum', models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_book', to='books.BookType', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '书籍版块类别',
                'verbose_name_plural': '书籍版块类别',
                'db_table': 'GX_book_type',
            },
        ),
        migrations.AddField(
            model_name='bookdetail',
            name='book_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='books.BookType', verbose_name='所属类别'),
        ),
    ]
