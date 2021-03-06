#! /usr/bin/env python

import os
from app import create_app, db
from app.models import User, Role, Permission, Post, Follow, Comment
from flask_script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission, Post=Post, Follow=Follow, Comment=Comment)


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
    # db.create_all()
