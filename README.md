# guoxue
前端基于vue的，后端基于django+django_rest_framework的论坛系统

# 项目描述

本项目是一个前后端分离的论坛系统。前端基于vue.js框架的，后端基于django+django_rest_framework，前后端之间通过vue.js的axios发送http请求获取数据，实现交互。

![image](https://raw.githubusercontent.com/123success123/jinxixi/master/images/homepages.png)

# 项目使用说明

因为本项目仅仅只是自己编写的一个小项目，项目里面使用到的第三方接口都是测试接口，因此是有过期时间的。比如说七牛云的图片存储接口是有过期时间，如果要永久性使用的话，需要本人去进行相应的实名认证操作。由于本人没有去进行实名操作，因此本项目中的七牛云测试接口过不久将会过期。因此一旦超过这个期限，本项目将没办法供其他用户下载后运行使用。所以本项目不提供运行说明。本项目仅供思路参考，以及部分功能业务设计。

# 项目功能模块总结

	1. 电子产品  B2B2C  PC电脑端网页
	2. 功能模块：用户模块  商品模块（首页、 搜索、商品） 购物车模块  订单模块（下单、 支付）
	3. 买家模块：注册、登录、激活（待搞）、退出、个人信息管理、收货地址管理、订单管理（收货等）
	4. 卖家模块：注册、登录、激活（待搞）、退出、个人信息管理、商品管理、订单管理
	5. 商品模块：首页、详情、列表、搜索（haystack+whoosh）
	6. 购物车： 增加、删除、修改、查询
	7. 订单模块：确认订单页面、提交订单（下单）、请求支付、查询支付结果
	8. itsdangerous  生成签名的token （序列化工具 dumps  loads）
	9. 邮件 （django提供邮件支持 配置参数  send_mail）
	10. celery (重点  整体认识 异步任务)
	11. 缓存（缓解压力， 保存的位置、有效期、与数据库的一致性问题）
	12. 搜索（ whoosh  索引  分词）
	13. ajax 前端用ajax请求后端接口
	14. 事务
	15. 高并发的库存问题 （悲观锁、乐观锁）
	16. 七牛云、支付宝接口的使用

# 项目难点

	1. 订单的处理： 在订单处理中涉及到了多表操作以及订单的并发处理问题（乐观锁、悲观锁等的使用）
	2. 全文检索的使用
	3. 支付宝接口以及七牛云接口的使用
	4. celery的使用

# 项目缺点

	1. 应该直接使用django内置的auth和permission来进行管理。而不是自己设置权限表和自定义用户登录
	2. 没有对商品进行更加细致的分类。比如商品的sku和spu
	3. 字段，以及方法的命名不规范。大部分都是采用中文拼音来命名的
	4. 对于订单订单表中的后面那四个字段（支付、发货、收货、完成）其实可以通过一个choicefield字段来完成，而不需要定义四个字段
 	5. 没有使用统一的自定义好的状态码来返回信息
