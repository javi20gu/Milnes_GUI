
from setting_GUI.database.run_datebase import Database


def login(email: str, password: str):

    usuarios = Database.usuarios()

    usuario = list(filter(lambda datos: datos[0] == email and datos[1] == password, usuarios))
    if usuario != []:
        return [True, Database.buscar_por_email(email)]
    else: 
        return [False]
