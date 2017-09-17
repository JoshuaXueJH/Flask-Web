from . import main
from flask import render_template, redirect, url_for
from flask_login import current_user
from .forms import PostForm
from ..models import Permission, Post
from .. import db


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    return render_template('index.html', form=form)
