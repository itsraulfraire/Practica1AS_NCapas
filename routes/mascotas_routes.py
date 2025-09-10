from flask import Blueprint, request, jsonify, render_template
from services.mascotas_service import listar_mascotas, buscar_mascotas, guardar_mascota

mascotas_bp = Blueprint("mascotas", __name__)

@mascotas_bp.route("/mascotas")
def mascotas_page():
    return render_template("mascotas.html")

@mascotas_bp.route("/tbodyMascotas")
def tbodyMascotas():
    mascotas = listar_mascotas()
    return render_template("tbodyMascotas.html", mascotas=mascotas)

@mascotas_bp.route("/mascotas/buscar")
def buscar():
    busqueda = request.args.get("busqueda", "")
    mascotas = buscar_mascotas(busqueda)
    return jsonify(mascotas)

@mascotas_bp.route("/mascota", methods=["POST"])
def guardar():
    mascota = {
        "idMascota": request.form.get("idMascota"),
        "nombre": request.form.get("nombre"),
        "sexo": request.form.get("sexo"),
        "raza": request.form.get("raza"),
        "peso": request.form.get("peso"),
        "condiciones": request.form.get("condiciones"),
    }
    guardar_mascota(mascota)
    return jsonify({"status": "ok"})

@mascotas_bp.route("/mascota/eliminar", methods=["POST"])
def eliminar():
    id_mascota = request.form.get("idMascota")
    if not id_mascota:
        return jsonify({"status": "error", "message": "Falta idMascota"}), 400

    ok = eliminar_mascota(id_mascota)
    if ok:
        return jsonify({"status": "ok", "id": id_mascota})
    return jsonify({"status": "error", "message": "No se pudo eliminar"}), 500
