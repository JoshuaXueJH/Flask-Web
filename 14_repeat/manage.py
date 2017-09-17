import os
from flask_script import Manager, Shell
from app import db, create_app
from app.models import Role, User, Comment, Post, Permission, Follow

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post, Comment=Comment, Permission=Permission, Follow=Follow)


manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
