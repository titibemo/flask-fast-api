from flask import Blueprint
import structlog
exercice1_bp = Blueprint('exercice1', __name__, url_prefix='/api/exercice1')

logger = structlog.get_logger()

@exercice1_bp.route('/hello/<language>', methods=['GET'])
def hello(language):
    logger.info('hello', language=language)
    return {
        'message': 'Hello',
        'language': language
    }

