from flask import render_template

from app import create_app

app = create_app()
with app.app_context():
    from flask_mail import Mail, Message
    from app.libs.email import generate_hash_and_token_url

    mail = Mail(app)
    redirect_url = generate_hash_and_token_url('web.index+index', hash='reset_password', token='11223414')
    content = render_template('email/reset_password.html', user_name='pppp', redirect_url=redirect_url)
    msg = Message(subject='reset', sender=app.config['MAIL_SENDER'], recipients=['1312342604@qq.com'])
    msg.html = content
    mail.send(msg)
