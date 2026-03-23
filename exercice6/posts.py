from flask import Blueprint, request, jsonify
from services.posts import get_current_time
import structlog
from flask_sqlalchemy import SQLAlchemy
import datetime
from .database import db
logger = structlog.get_logger()


###############  test sqlalchimu

class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    
####################

exercice6_bp = Blueprint('exercice6', __name__, url_prefix='/api/exercice6')

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
    posts = Post.query.all()
    return jsonify([{
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "created_at": post.created_at.isoformat(),
        "updated_at": post.updated_at.isoformat()
    } for post in posts])

@exercice6_bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    logger.info('get post request with id', id=id)
    for post in posts:
        if post["id"] == id:
            return jsonify(post)
    return jsonify({"error": "Article non trouvé"}), 404

# @exercice6_bp.route('/posts', methods=['POST'])
# def create_post():    
#     logger.info('create post request')
#     data = request.get_json()

#     if not data or not all(k in data for k in ("title", "content", "author")):
#         logger.error('missing json data')
#         return jsonify({"error": "Données invalides"}), 400

#     new_id = max(post["id"] for post in posts) + 1 if posts else 1

#     new_post = {
#         "id": new_id,
#         "title": data["title"],
#         "content": data["content"],
#         "author": data["author"],
#         "created_at": get_current_time(),
#         "updated_at": get_current_time()
#     }

#     posts.append(new_post)

#     return jsonify(new_post), 201

@exercice6_bp.route('/posts', methods=['POST'])
def create_post():
    logger.info("create post request")
    data = request.get_json()

    if not data or not all(k in data for k in ("title", "content", "author")):
        logger.error("missing json data")
        return jsonify({"error": "Données invalides"}), 400

    new_post = Post(
        title=data["title"],
        content=data["content"],
        author=data["author"],
        created_at=datetime.datetime.utcnow(),
        updated_at=datetime.datetime.utcnow()
    )

    db.session.add(new_post)
    db.session.commit()

    return jsonify({
        "title": new_post.title,
        "content": new_post.content,
        "author": new_post.author,
        "created_at": new_post.created_at.isoformat(),
        "updated_at": new_post.updated_at.isoformat()
    }), 201



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

