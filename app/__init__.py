from flask import Flask, render_template
from app.modules.auth import auth
from app.modules.houses import house
from app.modules.admin import admin


def create_app():
    app = Flask(__name__)
    app.secret_key = 'wef'
    app.register_blueprint(auth.bp)
    app.register_blueprint(house.bp)
    app.register_blueprint(admin.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    return app
