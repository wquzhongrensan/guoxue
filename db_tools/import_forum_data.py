import os
import sys


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append("/".join(pwd.split("/")[:-1]))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guoxue.settings")

import django
django.setup()

from forums.models import ForumType
from db_tools.data.forum_datas import forum_type_data

for lev1_forum in forum_type_data:
    forum_type = ForumType()
    forum_type.title = lev1_forum["title"]
    forum_type.forum_type = 1
    forum_type.save()

    for lev2_forum in lev1_forum["sub_forums"]:
        forum2_type = ForumType()
        forum2_type.title = lev2_forum["title"]
        forum2_type.forum_type = 2
        forum2_type.parent_forum = forum_type
        forum2_type.save()
