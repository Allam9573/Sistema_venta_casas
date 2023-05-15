from flask import render_template, request, Blueprint, redirect, url_for
from app.modules.db.db import get_connection
from app.modules.models.House import House

bp = Blueprint('house', __name__, url_prefix='/house')


@bp.route('/register', methods=['POST', 'GET'])
def register_house():
    if request.method == 'POST':
        direccion = request.form['direccion']
        propietario = request.form['propietario']
        precio = request.form['precio']
        url_foto = request.form['foto']
        house = House(direccion, propietario, precio, url_foto)
        con = get_connection()
        cursor = con.cursor(buffered=True)
        query = "INSERT INTO casas(direccion,propietario,precio,foto) VALUES(%s,%s,%s,%s)"
        cursor.execute(query, (house.get_direccion(
        ), house.get_propietario(), house.get_precio(), house.get_foto()))
        con.commit()
    return render_template('house/house_register.html')


@bp.route('/houses')
def list_houses():
    con = get_connection()
    cursor = con.cursor(buffered=True)
    cursor.execute('SELECT * FROM casas ORDER BY direccion ASC')
    con.commit()
    data = cursor.fetchall()
    return render_template('house/list_houses.html', data=data)


@bp.route('/edit_info/<id>')
def edit_info(id):
    con = get_connection()
    cursor = con.cursor(buffered=True)
    cursor.execute('SELECT * FROM casas WHERE id=%s', [id])
    con.commit()
    data = cursor.fetchall()
    return render_template('house/edit_house.html', data=data[0])


@bp.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id = int(request.form['id'])
        direccion = request.form['direccion']
        propietario = request.form['propietario']
        precio = request.form['precio']
        foto = request.form['foto']
        con = get_connection()
        cursor = con.cursor(buffered=True)
        cursor.execute('UPDATE casas SET direccion=%s, propietario=%s, precio=%s, foto=%s WHERE id=%s',
                       (direccion, propietario, precio, foto, id))
        con.commit()
        return redirect(url_for('house.success'))


@bp.route('/edit_success')
def success():
    return render_template('house/edit_success.html')


@bp.route('/delete_success')
def remove_success():
    return render_template('house/remove_success.html')


@bp.route('/delete_house/<id>')
def house_delete(id):
    con = get_connection()
    cursor = con.cursor(buffered=True)
    cursor.execute('DELETE FROM casas WHERE id=%s', [id])
    con.commit()
    return redirect(url_for('house.remove_success'))
