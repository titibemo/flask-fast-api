from flask import Blueprint, request, jsonify
import structlog
logger = structlog.get_logger()
exercice3_bp = Blueprint('exercice3', __name__, url_prefix='/api/exercice3')

# Créez une API simple pour gérer une liste de livres en mémoire.

# Routes:
# - `GET /books` - Retourner tous les livres
# - `GET /books/<id>` - Retourner un livre par ID
# - `POST /books` - Ajouter un nouveau livre

exercice3_bp = Blueprint('exercice3', __name__, url_prefix='/api/exercice3')

books = [
    {
        "id": 1,
        "title": "Le Petit Prince",
        "author": "Antoine de Saint-Exupéry",
        "year": 1943
    },
    {
        "id": 2,
        "title": "Le Rouge et le Noir",
        "author": "Stendhal",
        "year": 1830
    }
]

@exercice3_bp.route('/books', methods=['GET'])
def get_books():
    logger.info('get books request')
    return jsonify(books)

@exercice3_bp.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    logger.info('get book request', id=id)
    for book in books:
        if book["id"] == id:
            return jsonify(book)
    return jsonify({"error": "Livre non trouvé"}), 404

@exercice3_bp.route('/books', methods=['POST'])
def create_book():
    logger.info('create book request')
    data = request.get_json()

    if not data or not all(k in data for k in ("title", "author", "year")):
        return jsonify({"error": "Données invalides"}), 400

    new_id = max(book["id"] for book in books) + 1 if books else 1

    new_book = {
        "id": new_id,
        "title": data["title"],
        "author": data["author"],
        "year": data["year"]
    }

    books.append(new_book)

    return jsonify(new_book), 201