from repositories.usuarios_repository import autenticar_usuario

def iniciar_sesion(usuario, contrasena):
    user = autenticar_usuario(usuario, contrasena)
    if user:
        # Aquí podrías generar un token, guardar sesión, etc.
        return {"status": "ok", "user": user}
    return {"status": "error", "message": "Usuario y/o Contraseña incorrectos"}
