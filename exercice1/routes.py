from flask import Blueprint
exercice1_bp = Blueprint('exercice1', __name__, url_prefix='/api/exercice1')

@exercice1_bp.route('/hello/<language>', methods=['GET'])
def hello(language):
    return {
        'message': 'Hello',
        'language': language
        }

