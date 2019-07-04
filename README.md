# guoxue
前端基于vue的，后端基于django+django_rest_framework的论坛系统

# 项目描述

本项目是一个前后端分离的以国学为主题的论坛系统。前端基于vue.js框架的，后端基于django+django_rest_framework，前后端之间通过vue.js的axios发送http请求获取数据，实现交互。

![image](https://raw.githubusercontent.com/123success123/guoxue/master/images/person.png)

# 项目使用说明

本项目仅供思路参考，以及论坛相关的功能业务诸如发帖、回帖等的数据库设计以及功能设计。

# 项目功能模块总结

	1. 论坛   PC电脑端网页
	2. 功能模块：用户模块 论坛模块（发帖、回帖、点赞、收藏、浏览）  书籍推荐模块（浏览）   文章模块（浏览）
	3. 用户模块：注册、登录、激活、退出、关注、个人信息管理、个人论坛管理管理（删帖、发帖、回帖）、个人收藏、关注等管理
	4. 论坛模块：首页、详情、列表、发帖、回帖、点赞、收藏、浏览
	5. 书籍推荐模块： 首页、详情页、浏览
	6. 文章模块：首页、列表页、详情页、浏览
	7. django默认的认证系统 AbstractUser ，同时采用jwt实现用户登录认证。
	8. itsdangerous生成签名的token，用户生成用户账号激活的token信息
	9. 邮件（django提供邮件支持  配置参数  send_mail）
	10. 缓存（drf-extention）（缓解压力， 保存的位置、有效期、与数据库的一致性问题）
	11. 前端采用vue实现，用到了其中的axios来发送ajax请求获取数据、vuex来存储数据、router来实现页面展示。

# 项目难点

	1.跨域问题：
	当时在操作的时候，由于是第一次解决跨域问题。就按照教程一步一步配置，等到按照教程配置完成之后，本来以为就好了。但是一部还是报跨域失败的错误后来就百度、谷歌解决解决这个问题。搞了差不多2个多小时。最后，我再前端的请求ul的末尾添加上一个反斜杠，然后请求就发送成功了。
	2.我觉得项目的难点就是在xadmin、ueditor等组件的配置上。因为这个项目，其实说实话。业务逻辑不复习。就是普通论坛的发帖、回帖、点赞、收藏、关注等，然后其他的部分就是浏览功能了。

# 项目特点

	1. 采用的基于cbv，即class-base-view，基于类的视图，来进行开发
	2. django+django_rest_framework
	3. 集成了富文本编辑器ueditor
	4. 使用了缓存缓存数据,同时对sql语句进行了一定的优化。
	5. 登录验证方式采用的不是drf内置的token认证方式，而采用的是jwt认证方式
	6. 继承django内置的abstractuser类实现user模型类
	7. 使用到了drf的viewset、serializer、modelserializer、filter、pagination、throtting等来实现后端视图的开发

# 项目缺点

	1.异常处理没有做好。有的有，有的没有。而且对于异常处理。应该分开不同的业务捕获不同的异常。比如查询goodinfo的和查询userinfo的应该分开try，然后如果错误了就应该返回不同的状态提示码。同时注意，捕获异常时，应该尽量捕获指定的异常，而不是直接捕获Exception。这样子才能够根据指定的异常进行相应的操作。
	2.在编写serializer时，应该尽量满足单一职责原则。应该尽量让serializer就序列化当前对应的model对象即可。而对于要修改其他模型类中的数据的话，则需要放到viewset中去
