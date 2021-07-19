from db import get_db
from flask import render_template, session, abort, request, flash, url_for, redirect, Blueprint

posts_page = Blueprint('posts_page', __name__, template_folder='templates')


@posts_page.route('/posts')
def get():
    db = get_db()
    cur = db.execute('select * from posts order by id desc')
    posts = cur.fetchall()
    return render_template('posts.html', posts=posts)


@posts_page.route('/posts', methods=['POST'])
def post():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into posts (title, text) values (?, ?)',
               [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('posts_page.get'))
