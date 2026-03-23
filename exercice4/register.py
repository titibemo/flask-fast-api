from flask import Blueprint, request, jsonify
from services.users import validate_username, validate_email, validate_password, validate_age
import structlog

logger = structlog.get_logger()

exercice4_bp = Blueprint('exercice4', __name__, url_prefix='/api/exercice4')

users = []

@exercice4_bp.route('/register', methods=['POST'])
def register():
    logger.info('register request')
    data = request.get_json()
    errors = []

    if not data:
        logger.error('missing json data')
        return jsonify({"errors": ["Données JSON requises"]}), 400

    # validations
    username_error = validate_username(data.get("username"))
    email_error = validate_email(data.get("email"))
    password_error = validate_password(data.get("password"))
    age_error = validate_age(data.get("age"))

    for err in [username_error, email_error, password_error, age_error]:
        if err:
            logger.error('validation error', err=err)
            errors.append(err)

    if errors:
        return jsonify({"errors": errors}), 400

    new_user = {
        "username": data["username"],
        "email": data["email"],
        "password": data["password"],
        "age": data["age"]
    }

    users.append(new_user)

    return jsonify(new_user), 201