from flask import Blueprint, request
exercice2_bp = Blueprint('exercice2', __name__, url_prefix='/api/exercice2')

@exercice2_bp.route('/convert/temp', methods=['GET'])
def temperature():
    value = request.args.get('value', type=float)
    unit = request.args.get('unit', type=str)
    if value is None or unit is None:
        return {"error": "Paramètres 'value' et 'unit' requis"}, 400

    if unit == "c2f":
        fahrenheit = (value * 9/5) + 32
        return {
            "celsius": value,
            "fahrenheit": round(fahrenheit, 2)
        }

    elif unit == "f2c":
        celsius = (value - 32) * 5/9
        return {
            "fahrenheit": value,
            "celsius": round(celsius, 2)
        }

    else:
        return {"error": "Unité invalide (c2f ou f2c)"}, 400