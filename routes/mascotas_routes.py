from flask import Blueprint, render_template
from services.mascota_service import obtener_mascotas

mascotas_bp = Blueprint("mascotas", __name__)

@mascotas_bp.route("/tbodyMascotas")
def tbody_mascotas():
    mascotas = obtener_mascotas()
    return render_template("tbodyMascotas.html", mascotas=mascotas)
