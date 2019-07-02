"""guoxue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

import xadmin
from django.urls import path, include, re_path
from django.views.static import serve
from django.views.generic.base import TemplateView
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views  import obtain_jwt_token
from rest_framework.schemas import get_schema_view

from books.views import BookTypeMsgs, BookDetailMsgs, BookHomepages, BookSortHomepages
from articles.views import Article_RM_Msgs, Article_JR_Msgs, Article_ZW_Msgs, Article_GR_Msgs, Article_GR_Detail_Msgs, \
    Article_Detail_Msgs
from users.views import UserRegViewsets, UserInfoViewsets, UserIDInfo, UserId, UserLoginThirdparty, UserConfirmViewset
from forums.views import ForumTypeMsgs, ForumCreateTopicViewsets, ForumTopicDetailViewsets, \
    ForumReplyViewsets, ForumHonorViewsets, ForumIndexDetail, ForumDetailReply, ForumDetail
from forums.controller import handler
from user_operation.views import UserFavViewset, UserFollowViewset
from guide.views import GuideTypeMsgs, GuideDetailMsgs
# 自定义ｊｗｔ
from utils import jwt_handle

# 初始化配置参数
ROOT = os.path.dirname(__file__)
schema_view = get_schema_view(title='Schema API')

# 使用router来配合viewset
router = DefaultRouter()

# 获取书籍分类信息    books_detail_at/77/
router.register('book_types', BookTypeMsgs, base_name="books_types")
# 获取书籍详情
router.register('book_msgs', BookDetailMsgs, base_name="book_msgs")
# 获取首页的书籍信息
router.register('book_homepages', BookHomepages, base_name="book_homepages")
# 获取首页的书籍排名信息
router.register('book_sort_homepages', BookSortHomepages, base_name="book_sort_homepages")

# 指南信息
router.register("guide_type_msgs", GuideTypeMsgs, base_name="guide_type_msgs")
router.register("guide_detail_msgs", GuideDetailMsgs, base_name="guide_detail_msgs")

# 获取首页国学入门的信息
router.register('article_rm_msgs', Article_RM_Msgs, base_name="article_rm_msgs")
# 获取首页今日国学的信息
router.register('article_jr_msgs', Article_JR_Msgs, base_name="article_jr_msgs")

# 获取哲学文化的文章信息   /article_zw_msgs/8-11/
router.register('article_zw_msgs', Article_ZW_Msgs, base_name="article_zw_msgs")
# 获取国学人物的信息   /article_gr_msgs/45-47/
router.register('article_gr_msgs', Article_GR_Msgs, base_name="article_gr_msgs")

# 获取国学人物的详细信息   /article_grd_msgs/1/
router.register('article_grd_msgs', Article_GR_Detail_Msgs, base_name="article_grd_msgs")

# 获取文章的详细信息   /article_d_msgs/6/
router.register('article_d_msgs', Article_Detail_Msgs, base_name="article_d_msgs")

# 用户注册接口
router.register("users", UserRegViewsets, base_name="users")
# 获取用户的id
router.register("users_id", UserId, base_name="users_id")

# 修改个人信息
router.register("person_infos", UserInfoViewsets ,base_name="person_infos")
# 通过用户名获取用户信息
router.register("person_info", UserIDInfo , base_name="person_info")

# 获取论坛分类信息
router.register("forum_type_msgs", ForumTypeMsgs, base_name="forum_type_msgs")
# 用户发帖
router.register("forum_topics", ForumCreateTopicViewsets, base_name="forum_topics")
# 获取帖子详情
router.register("forum_msgs", ForumTopicDetailViewsets, base_name="forum_msgs")
# 用户回帖
router.register("forum_reply_msgs", ForumReplyViewsets, base_name="forum_reply_msgs")
# 展示论坛排名信息
router.register("forum_honor_msgs", ForumHonorViewsets, base_name="forum_honor_msgs")
# 获取论坛帖子信息
router.register("forum_detail_msgs", ForumIndexDetail, base_name="forum_detail_msgs")
# 获取回帖信息
router.register("forum_detail_reply_msgs", ForumDetailReply, base_name="forum_detail_reply_msgs")
# 获取简单的帖子信息
router.register("forum_part_detail_msgs", ForumDetail, base_name="forum_part_detail_msgs")

# 用户操作--收藏
router.register("userfav_msgs", UserFavViewset, base_name="userfav_msgs")
# 用户关注功能
router.register("userfollow_msgs", UserFollowViewset, base_name="userfolow_msgs")

# sentry test
# def trigger_error(request):
#     division_by_zero

urlpatterns = [
    # 配置访问xadmin后台管理系统的
    path('managements/', xadmin.site.urls),
    # 配置django+drf项目关联vue项目,实现"/"直接关联到index.html页面
    re_path(r'^$', TemplateView.as_view(template_name='index.html')),
    # 配置后台访问静态文件的  eg:img
    re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    # 配置生产环境下也就是debug=false时，还是让django帮我们处理到静态文件的（除非使用了nginx）
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    # 配置drf的登录入口
    path('api-auth/', include(('rest_framework.urls', 'rest_framework'), namespace='rest_framework')),
    # 配置显示ＡＰＩ接口的概要界面
    path('schemas/', schema_view),
    # 配置显示ＡＰＩ接口的文档界面
    path('docs/', include_docs_urls(title="国学之家")),
    # 配置ｒｏｕｔｅｒ
    path('', include(router.urls)),

    # jwt用户登录接口， 返回token信息　　自定义了ｊｗｔ，添加了返回的信息
    re_path(r'sessions/$', jwt_handle.CustomizeJObtainJSONWebToken.as_view()),
    # 用户账号确认
    re_path("account_numbers/(.*)/", UserConfirmViewset.as_view()),
    # 配置的第三方登录
    path('', include('social_django.urls', namespace='social')),
    # 定义用户通过第三方认证之后的回调
    path('login_done', UserLoginThirdparty.as_view(), name="login_done"),

    # 配置在后台可以访问到ueditor富文本编辑器的
    path('ueditor/', include('DjangoUeditor.urls')),
    # 配置前端ueditor图片的上传url--前端请求的处理视图
    path('ue_upload2/',handler, name="ue_upload2"),
    # 配置ueditor.json文件中配置的静态文件上传路径
    re_path('upload/(?P<path>.*)', serve, {"document_root": (ROOT+"/media").replace('\\','/')}),

    # sentry test
    # 注意，配置好sentry之后，用户所有的bug，如果自己没有捕获的话，不出意外，应该都会发送到sentry中去。 当然前提是服务器有开启
    # path('sentry_debug/', trigger_error),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
