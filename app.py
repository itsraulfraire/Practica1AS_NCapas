from flask import Flask, render_template
from flask_cors import CORS
from routes.mascotas_routes import mascotas_bp
from routes.usuarios_routes import usuarios_bp

app = Flask(__name__)
CORS(app)

# Registrar Blueprints
app.register_blueprint(mascotas_bp)
app.register_blueprint(usuarios_bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/app")
def login_page():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

