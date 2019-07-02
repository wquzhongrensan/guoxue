from django.conf import settings
from django.core.mail import send_mail


class HandleMail(object):
    """
    发送邮件确认用户账号
    """

    def send_mail_for_confirm(self, token, mail, username):
        msg='<a href="{0}/account_numbers/{1}/">点击激活账号--{2}</a>'.format(settings.LOCALHOST, token, username)
        send_mail('注册激活','',settings.EMAIL_FROM,
            [mail],
            html_message=msg
        )
