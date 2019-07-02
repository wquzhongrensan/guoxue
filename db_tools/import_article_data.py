import os
import sys


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append("/".join(pwd.split("/")[:-1]))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guoxue.settings")

import django
django.setup()

from articles.models import ArticleType
from db_tools.data.article_data import article_type_data

# 添加book类别信息
for lev1_art in article_type_data:
    article_type = ArticleType()
    article_type.title = lev1_art["title"]
    article_type.article_types = 1
    article_type.save()

    for lev2_art in lev1_art["sub_article_types"]:
        article2_type = ArticleType()
        article2_type.title = lev2_art["title"]
        article2_type.article_types = 2
        article2_type.parent_article = article_type
        article2_type.save()

        for lev3_art in lev2_art["sub_article_types"]:
            article3_type = ArticleType()
            article3_type.title = lev3_art["title"]
            article3_type.article_types = 3
            article3_type.parent_article = article2_type
            article3_type.save()

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