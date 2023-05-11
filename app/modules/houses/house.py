from flask import Flask, render_template, request, Blueprint
from app.modules.db.db import get_connection

bp = Blueprint('house',__name__, '/house')

@bp.route('/register', methods=['POST','GET'])
def register_house():
    if request.method == 'POST':
        direccion = request.form['direccion']
        return render_template('')
