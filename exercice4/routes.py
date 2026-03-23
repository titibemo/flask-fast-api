from flask import Blueprint, request, jsonify
exercice4_bp = Blueprint('exercice4', __name__, url_prefix='/api/exercice4')

from flask import Blueprint, request, jsonify
import re

exercice4_bp = Blueprint('exercice4', __name__, url_prefix='/api/exercice4')

users = []

def validate_username(username):
    if not username:
        return "Username requis"
    if not (2 <= len(username) <= 20):
        return "Username doit contenir entre 2 et 20 caractères"

def validate_email(email):
    if not email:
        return "Email requis"
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern, email):
        return "Email invalide"

def validate_password(password):
    if not password:
        return "Password requis"
    if len(password) < 8:
        return "Password doit contenir au moins 8 caractères"

def validate_age(age):
    if age is None:
        return "Age requis"
    if not isinstance(age, int):
        return "Age doit être un entier"
    if not (18 <= age <= 100):
        return "Age doit être entre 18 et 100"

@exercice4_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    errors = []

    if not data:
        return jsonify({"errors": ["Données JSON requises"]}), 400

    # validations
    username_error = validate_username(data.get("username"))
    email_error = validate_email(data.get("email"))
    password_error = validate_password(data.get("password"))
    age_error = validate_age(data.get("age"))

    for err in [username_error, email_error, password_error, age_error]:
        if err:
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