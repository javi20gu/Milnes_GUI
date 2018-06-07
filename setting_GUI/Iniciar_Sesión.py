
import sqlite3


def login(email: str, password: str):

    root = sqlite3.connect("login.db")
    cursor = root.cursor()

    autentificado: bool = False

    cursor.execute("SELECT Email, Password FROM login")
    usuarios = cursor.fetchmany(-1)

    for usuario in usuarios:
        if usuario[0] == email and usuario[1] == password:
            autentificado = True
            cursor.execute("SELECT * FROM login WHERE Email='{}'".format(usuario[0]))
            e = cursor.fetchone()
            root.commit()
            root.close()
            return True, e

    if not autentificado:
        return [False]

    root.commit()
    root.close()
