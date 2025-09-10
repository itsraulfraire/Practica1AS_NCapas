from flask import Blueprint, render_template

app_bp = Blueprint("app", __name__)

@app_bp.route("/")
def index():
    return render_template("login.html")

@app_bp.route("/mascotas")
def mascotas():
    return render_template("mascotas.html")
