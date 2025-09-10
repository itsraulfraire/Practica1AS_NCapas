from flask import Blueprint, request, render_template, jsonify
from services.mascotas_service import crear_mascota, eliminar_mascota, obtener_mascotas

mascotas_bp = Blueprint("mascotas", __name__)

@mascotas_bp.route("/mascotas")
def mascotas():
    return render_template("mascotas.html")

@mascotas_bp.route("/tbodyMascotas")
def tbody_mascotas():
    mascotas = obtener_mascotas()
    return render_template("tbodyMascotas.html", mascotas=mascotas)

@mascotas_bp.route("/mascota", methods=["POST"])
def crear():
    datos = request.form
    crear_mascota(datos)
    return "OK"

@mascotas_bp.route("/mascota/eliminar", methods=["POST"])
def eliminar():
    id_mascota = request.form.get("idMascota")
    eliminar_mascota(id_mascota)
    return "OK"
