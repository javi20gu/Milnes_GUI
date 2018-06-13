
from setting_GUI.database.run_datebase import Database


def login(email: str, password: str):

    autentificado: bool = False

    usuarios = Database.usuarios()

    for usuario in usuarios:
        if usuario[0] == email and usuario[1] == password:
            autentificado = True
            e = Database.buscar_por_email(email)
            return autentificado, e

    if not autentificado:
        return [autentificado]
