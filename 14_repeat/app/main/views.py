from . import main
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from .forms import PostForm, EditProfileForm
from ..models import Permission, Post, User
from .. import db


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    return render_template('index.html', form=form)


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('user.html', user=user, posts=posts)


@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)

@main.route('/edit_profile/<int:id>')
@login_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form =


@main.route('/followers/<username>')
def followers(username):
    user = User.filter_by(username=username).first()
    if user is None:
        flash('Invalid user.')
        return redirect(url_for('.index'))


@main.route('/followed_by/<username>')
def followed_by(username):
    user = User.filter_by(username=username)
    if user is None:
        flash('Invalid user.')
        return redirect(url_for('.index'))
