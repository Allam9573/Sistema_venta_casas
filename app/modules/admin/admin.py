from flask import Blueprint, render_template
from app.modules.db.db import get_connection

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/houses_list')
def houses_list():
    con = get_connection()
    cursor = con.cursor(buffered=True)
    cursor.execute('SELECT * FROM casas')
    con.commit()
    data = cursor.fetchall()
    return render_template('house/admin_list.html', data=data)
