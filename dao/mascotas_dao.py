from db import get_db

def listar_mascotas():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM mascotas")
    rows = cursor.fetchall()

    mascotas = []
    for row in rows:
        mascotas.append({
            "idMascota": row[0],
            "nombre": row[1],
            "sexo": row[2],
            "raza": row[3],
            "peso": row[4],
            "condiciones": row[5]
        })

    return mascotas

def insertar_mascota(datos):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO mascotas (nombre, sexo, raza, peso, condiciones)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        datos["nombre"],
        datos["sexo"],
        datos["raza"],
        datos["peso"],
        datos["condiciones"]
    ))
    db.commit()

def borrar_mascota(id_mascota):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM mascotas WHERE idMascota = %s", (id_mascota,))
    db.commit()
