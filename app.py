# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from exercice1.exercice1_road import exercice1_bp
from exercice2.temperature import exercice2_bp
from exercice3.books import exercice3_bp
from exercice4.register import exercice4_bp
from exercice5.calculate import exercice5_bp
from exercice6.posts import exercice6_bp
from services.logger import setup_logging
from exercice6.database import db

setup_logging()

app = Flask(__name__)
app.register_blueprint(exercice1_bp) 
app.register_blueprint(exercice2_bp)
app.register_blueprint(exercice3_bp)
app.register_blueprint(exercice4_bp)
app.register_blueprint(exercice5_bp)
app.register_blueprint(exercice6_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tata:secret@localhost:8001/utilisateur'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) 

if __name__ == '__main__':
    app.run(debug=True, port=5000)