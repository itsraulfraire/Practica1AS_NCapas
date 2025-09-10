from flask import Blueprint, request, session, jsonify
from services.usuario_service import validar_usuario

login_bp = Blueprint("login", __name__)

@login_bp.route("/iniciarSesion", methods=["POST"])
def iniciar_sesion():
    usuario = request.form.get("txtUsuario")
    contrasena = request.form.get("txtContrasena")
    
    if validar_usuario(usuario, contrasena):
        session["usuario"] = usuario
        return jsonify({"ok": True})
    
    return jsonify({})
