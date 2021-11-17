from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from ..auth import bp
from ..models import User
from .forms import LoginForm

@bp.route('/login', methods=['GET', 'POST'])
def login():
    
    #We can't login in twice
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()

    if not form.is_submitted():
        return render_template('login.html', form=form)
    
    if not form.validate():
        print("Invalid form")
        flash("Invalid Form")
        return render_template('login.html', form=form)
    
    username = form.username.data
    password = form.password.data
    remember_me = form.remember_me.data
    user = User.get_user(username)

    if user is None:
        #Leaking username, will need to change in the future
        print("Invalid username")
        flash("Invalid Username")
        return render_template('login.html', form=form)

    if not user.check_password(password):
        #Again leaking information
        print("Invalid password")
        flash("Invalid Password")
        return render_template('login.html', form=form)

    else:
        login_user(user, remember=remember_me)
        print("Logged in")
        flash("Logged In")
        return redirect(url_for('main.index'))

@bp.route('/logout')
def logout():
    logout_user()
    flash("Logged Out")
    return redirect(url_for('main.index'))