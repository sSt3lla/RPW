from flask import render_template, redirect, url_for
from ..auth import bp
from .forms import LoginForm

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('Login requested for user={}, password={}. remember_me={}'.format(
            form.username.data, form.password.data, form.remember_me.data))
        return redirect(url_for('main.index'))

    return render_template('login.html', form=form)