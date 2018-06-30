"""
@Created by Seven on 2018-06-07
import os
from flask import (Flask,request....)
"""
# import smtplib
# from email.mime.text import MIMEText
from threading import Thread

from flask import current_app, render_template, url_for

from flask_mail import Mail, Message

mail = Mail()
from app.libs.error_code import EmailException


# class Email:
#     __user = current_app.config['MAIL_USERNAME']
#     __password = current_app.config['MAIL_PASSWORD']
#     __host = current_app.config['MAIL_SERVER']
#
#     @classmethod
#     def send_reset_password_email(cls, email_address, email_title, token, user_name, template=None):
#         redirect_url = generate_hash_and_token_url('web.index+index', hash='reset_password', token=token)
#         content = render_template(template, user_name=user_name, redirect_url=redirect_url)
#         msg = MIMEText(content, _subtype='html', _charset='utf-8')
#         thr = Thread(target=cls.send_email_async, args=[cls, msg, email_address, email_title])
#         thr.start()
#         return thr
#
#     @classmethod
#     def send_html(cls, to_user, sub, template=None, **kwargs):
#         content = render_template(template, **kwargs)
#         msg = MIMEText(content, _subtype='html', _charset='utf-8')
#         thr = Thread(target=cls.send_email_async, args=[cls, msg, to_user, sub])
#         thr.start()
#         return thr
#
#     @classmethod
#     def send_text(cls, to_user, sub, text=None):
#         msg = MIMEText(text, _charset='utf-8')
#         thr = Thread(target=cls.send_email_async, args=[cls, msg, to_user, sub])
#         # cls.send_email_async(msg, to_user, sub)
#         thr.start()
#         return thr
#
#     def send_email_async(self, msg, to_user, sub):
#         __me = "<" + self.__user + ">"
#
#         msg['Subject'] = sub
#         msg['From'] = __me
#         msg['To'] = to_user
#         try:
#             # self.server = smtplib.SMTP(host=self.__host, port=80)
#             server = smtplib.SMTP_SSL(host=self.__host, port=465)
#             # server.connect(self.__host, 80)
#             # server.set_debuglevel(1)
#             server.login(self.__user, self.__password)
#             server.sendmail(__me, to_user, msg.as_string())
#             server.quit()
#         except EmailException as e:
#             raise e(msg="邮件发送异常", code=10027)
#         # server.close()
#
#     # 析构函数:释放资源
#     # def __del__(self):
#     #     self._server.quit()
#     #     self._server.close()


def send_reset_password_email(email_address, email_title, token, user_name, template=None):
    app = current_app._get_current_object()
    redirect_url = generate_hash_and_token_url('web.index+index', hash='reset_password', token=token)
    content = render_template(template, user_name=user_name, redirect_url=redirect_url)
    msg = Message(subject=email_title, sender=app.config['MAIL_SENDER'], recipients=[email_address])
    msg.html = content
    try:
        mail.send(msg)
    except Exception as e:
        # app.logger.info("\n %s", e)
        raise EmailException()
    # thr = Thread(target=send_email_async, args=[app, msg])
    # thr.start()
    # return thr


def send_email_async(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            app.logger.info("\n %s", e)


def generate_hash_and_token_url(endpoint, hash, token):
    base_url = url_for(endpoint)
    return '{}#/{}?token={}'.format(base_url, hash, token)
