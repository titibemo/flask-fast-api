from flask import Blueprint, request, jsonify
import structlog
logger = structlog.get_logger()

exercice5_bp = Blueprint('exercice5', __name__, url_prefix='/api/exercice5')

# Créez une route `/calculate` qui accepte:
# - `operation`: "add", "subtract", "multiply", "divide"
# - `a`: premier nombre
# - `b`: deuxième nombre

exercice5_bp = Blueprint('exercice5', __name__, url_prefix='/api/exercice5')

@exercice5_bp.route('/calculate', methods=['POST'])
def calculate():
    logger.info('calculate request')
    data = request.get_json()
    operation = data.get('operation')
    a = data.get('a')
    b = data.get('b')

    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            return jsonify({"error": "Division par zero"}), 400
        result = a / b
    else:
        logger.error('invalid operation', operation=operation)
        return jsonify({"error": "Operation invalide"}), 400

    return jsonify({"result": result})
