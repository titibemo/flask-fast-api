from flask import Blueprint, request, jsonify
from services.posts import get_current_time
import structlog
logger = structlog.get_logger()

exercice6_bp = Blueprint('exercice6', __name__, url_prefix='/api/exercice6')

# Créez une API blog complète avec:
# - `GET /posts` - Lister tous les articles
# - `GET /posts/<id>` - Détail d'un article
# - `POST /posts` - Créer un article
# - `PUT /posts/<id>` - Modifier un article
# - `DELETE /posts/<id>` - Supprimer un article

posts = [
    {
        "id": 1,
        "title": "Mon premier article",
        "content": "Ceci est le contenu de mon premier article.",
        "author": "John Doe",
        "created_at": "2022-01-01",
        "updated_at": "2022-01-01"
    }
]

@exercice6_bp.route('/posts', methods=['GET'])
def get_posts():
    logger.info('get posts request')
    return jsonify(posts)

@exercice6_bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    logger.info('get post request with id', id=id)
    for post in posts:
        if post["id"] == id:
            return jsonify(post)
    return jsonify({"error": "Article non trouvé"}), 404

@exercice6_bp.route('/posts', methods=['POST'])
def create_post():    
    logger.info('create post request')
    data = request.get_json()

    if not data or not all(k in data for k in ("title", "content", "author")):
        logger.error('missing json data')
        return jsonify({"error": "Données invalides"}), 400

    new_id = max(post["id"] for post in posts) + 1 if posts else 1

    new_post = {
        "id": new_id,
        "title": data["title"],
        "content": data["content"],
        "author": data["author"],
        "created_at": get_current_time(),
        "updated_at": get_current_time()
    }

    posts.append(new_post)

    return jsonify(new_post), 201

@exercice6_bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):    
    logger.info('update post request with id', id=id)
    data = request.get_json()

    if not data or not all(k in data for k in ("title", "content", "author")):
        return jsonify({"error": "Données invalides"}), 400

    for post in posts:
        if post["id"] == id:
            post["title"] = data["title"]
            post["content"] = data["content"]
            post["author"] = data["author"]
            post["updated_at"] = get_current_time()
            return jsonify(post)

    return jsonify({"error": "Article non trouvé"}), 404

@exercice6_bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    logger.info('delete post request with id', id=id)
    for post in posts:
        if post["id"] == id:
            posts.remove(post)
            return jsonify({"message": "Article supprimé"}), 200

    return jsonify({"error": "Article non rencontré"}), 404

