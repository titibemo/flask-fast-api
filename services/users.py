import re

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