# app.py
from flask import Flask
from exercice1.routes import exercice1_bp
from exercice2.routes import exercice2_bp
from exercice3.routes import exercice3_bp


app = Flask(__name__)
app.register_blueprint(exercice1_bp) 
app.register_blueprint(exercice2_bp)
app.register_blueprint(exercice3_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)