from flask import request, render_template, Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login')
def login():
    return render_template('auth/login.html')


@bp.route('/register')
def register():
    return render_template('auth/register.html')
