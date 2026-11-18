import sqlite3

def get_connection():
    conn = sqlite3.connect("equipo.db")
    return conn

def altura_media():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT AVG(altura) FROM jugadores WHERE fecha_baja IS NOT NULL")

    row = cursor.fetchone()

    altura_media = row[0]

    conn.close()

    return altura_media

def jugadores_altos():
    valor_altura_media = altura_media()

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT dni FROM jugadores WHERE fecha_baja IS null AND altura >= " + str(valor_altura_media))

    rows = cursor.fetchall()

    conn.close()

    with open("jugadores.txt", "wt") as f:
        for row in rows:
            f.write(row[0])
            

# MAIN
print("Altura media: ", altura_media())











