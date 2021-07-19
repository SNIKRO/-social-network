from flask import request, session, flash, redirect, url_for, render_template, Blueprint, current_app

users_page = Blueprint('users_page', __name__, template_folder='templates')


@users_page.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != current_app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != current_app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('posts_page.get'))
    return render_template('login.html', error=error)


@users_page.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('users_page.login'))
