import os
import sys


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append("/".join(pwd.split("/")[:-1]))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guoxue.settings")

import django
django.setup()

from guide.models import GuideType, GuideDetail
from db_tools.data.guide_date import guide_type_data, changyong

# 添加国学指南类别信息
# for lev1_guide in guide_type_data:
#     guide_type = GuideType()
#     guide_type.title = lev1_guide["title"]
#     guide_type.guide_type = 1
#     guide_type.save()
#
#     for lev2_guide in lev1_guide["sub_guide"]:
#         guide2_type = GuideType()
#         guide2_type.title = lev2_guide["title"]
#         guide2_type.guide_type = 2
#         guide2_type.parent_guide = guide_type
#         guide2_type.save()

# 天机常用网址的信息
for each in changyong:
    guide_detail = GuideDetail()
    guide_detail.title = each["title"]
    guide_detail.link = each["link"]
    guide_detail.guide_type_id = 14
    guide_detail.save()

