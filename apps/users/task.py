from celery import task

from utils import handle_mail


@task
def send_mail_confirms(token, u_mail, u_name):
    """发送邮件确认账号"""
    mail_handle = handle_mail.HandleMail()
    mail_handle.send_mail_for_confirm(token, u_mail, u_name)

# 自定义定时操作
@task
def del_redis_data():
    # 此处是一个删除redis数据的操作。具体略过
    print("del_redis_data")

@task
def back_up1():
    # 此处是一个备份到日报表的操作。具体略过
    print("back_up1")

@task
def back_up2():
    # 此处是一个生成统计报表的操作。具体略过
    print("back_up2")
