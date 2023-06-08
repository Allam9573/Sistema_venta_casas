from flask import Blueprint, render_template, request
from app.modules.db.db import get_connection

bp = Blueprint('admin', __name__, url_prefix='/admin')

con = get_connection()

@bp.route('/houses_list')
def houses_list():
    cursor = con.cursor(buffered=True)
    cursor.execute('SELECT * FROM casas')
    con.commit()
    data = cursor.fetchall()
    return render_template('house/admin_list.html', data=data)


@bp.route('/houses_list_id', methods=['POST','GET'])
def get_house_id():
    data = ''
    if request.method == 'POST':
        cursor = con.cursor(buffered=True)
        vendedor = request.form['buscar']
        cursor.execute('SELECT * FROM casas WHERE propietario=%s', [vendedor])
        data=cursor.fetchall()
    return render_template('house/admin_list.html', data=data)
