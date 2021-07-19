import os
from flask import Flask, g
from controllers.users import users_page
from controllers.posts import posts_page

config_path = os.path.join(os.path.dirname(__file__), 'config.json')

# создаём наше маленькое приложение :)
app = Flask(__name__)
app.config.from_json(config_path)
app.register_blueprint(users_page)
app.register_blueprint(posts_page)


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


if __name__ == '__main__':
    app.run()
