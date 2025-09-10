from flask import Flask, render_template
from controllers.mascotas_controller import mascotas_bp
from routes.app_routes import app_bp

app = Flask(__name__)
app.secret_key = "secreto"

# Registrar blueprint
app.register_blueprint(mascotas_bp)
app.register_blueprint(app_bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/app")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

