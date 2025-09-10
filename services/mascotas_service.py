from dao.mascotas_dao import insertar_mascota, borrar_mascota, listar_mascotas

def crear_mascota(datos):
    insertar_mascota(datos)

def eliminar_mascota(id_mascota):
    borrar_mascota(id_mascota)

def obtener_mascotas():
    return listar_mascotas()
