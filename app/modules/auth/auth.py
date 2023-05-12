from flask import request, render_template, Blueprint, session, redirect, url_for
from app.modules.models.User import User
from app.modules.db.db import get_connection
#from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasenia = request.form['contrasenia']
        con = get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute('SELECT * FROM usuarios WHERE usuario=%s AND CONTRASENIA=%s',(usuario, contrasenia))
        account = cursor.fetchone()
        if account:
            # session['logueado'] = True
            # session['id'] = account['id']
            return render_template('auth/profile.html', usuario = usuario)
        else: 
            return redirect(url_for('profile'))
    return render_template('auth/login.html')


@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        usuario = request.form['usuario']
        contrasenia = request.form['contrasenia']
        user = User(nombre, correo, usuario,contrasenia)
        con = get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute('INSERT INTO usuarios(nombre,correo,usuario,contrasenia) VALUES(%s,%s,%s,%s)',
                       (user.get_nombre(), user.get_correo(), user.get_usuario(), user.get_contrasenia()))
        con.commit()
    return render_template('auth/register.html')

@bp.route('/profile')
def profile():
    return render_template('auth/profile.html')
@bp.route('/create_account_success')
def success():
    return render_template('auth/success.html')
