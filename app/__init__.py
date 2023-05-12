from flask import Flask, render_template
from app.modules.auth import login
from app.modules.houses import house

def create_app():
    app = Flask(__name__)
    app.register_blueprint(login.bp)
    app.register_blueprint(house.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    return app
