import os
import sys


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append("/".join(pwd.split("/")[:-1]))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guoxue.settings")

import django
django.setup()

from books.models import BookType, BookAuthor
from db_tools.data.book_data import book_type_data, book_auth_data

# 添加book类别信息
# for lev1_cat in book_type_data:
#     book_type = BookType()
#     book_type.title = lev1_cat["title"]
#     book_type.book_type = 1
#     book_type.save()
#
#     for lev2_cat in lev1_cat["sub_books"]:
#         book2_type = BookType()
#         book2_type.title = lev2_cat["title"]
#         book2_type.book_type = 2
#         book2_type.parent_forum = book_type
#         book2_type.save()

# 添加作者信息
# for bookauth in book_auth_data:
#     book_auth = BookAuthor()
#     book_auth.name = bookauth["name"]
#     book_auth.introduce_link = bookauth["introduce_link"]
#     book_auth.introduces = bookauth["introduces"]
#     book_auth.avatar_link = bookauth["avatar_link"]
#     book_auth.save()

# 修改作者的头像
# author = BookAuthor.objects.filter()[:15]
# for each in author:
#     each.avatar_link = 'daodus/avatar_imgs/02_avatar.jpg'
#     each.save()
# author = BookAuthor.objects.filter()[15:]
# for each in author:
#     each.avatar_link = 'daodus/avatar_imgs/01_avatar.gif'
#     each.save()

# for each in BookType.objects.filter(book_type = 1):
#     for each1 in each.parent_forum:
#         print(each1)

# bookall = BookType.objects.filter(book_type = 1)
# print(bookall)
# bookall.delete()