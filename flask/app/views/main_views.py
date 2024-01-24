from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_app():
    return 'hello, app!'


@bp.route('/')
def index():
    return 'index Page'
