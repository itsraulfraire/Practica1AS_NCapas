from repositories.usuarios_repository import autenticar_usuario

def iniciar_sesion(usuario, contrasena):
    user = autenticar_usuario(usuario, contrasena)
    print("DEBUG >> Resultado de query:", user)
    if user is not None:
        return {"status": "ok", "user": user}
    return {"status": "error", "message": "Usuario y/o Contraseña incorrectos"}

