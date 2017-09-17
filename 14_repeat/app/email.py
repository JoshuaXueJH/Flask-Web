# -*- encoding: utf-8 -*-

from . import mail
from flask import current_app, render_template
from flask_mail import Message
from threading import Thread


def send_async_email(app, msg):
    """
    Flask-Mail中的send()函数使用current_app，因为必须激活程序上下文。
    不过，在不同的线程中执行mail.send()函数时，程序的上下文需要使用app.app_context()人工创建。
    """

    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    """Return the current object.  This is useful if you want the real
    object behind the proxy at a time for performance reasons or because
    you want to pass the object into a different context.
    """
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject, sender=app.config['FLASKY_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
