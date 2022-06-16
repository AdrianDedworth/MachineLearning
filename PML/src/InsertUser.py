from src.connect_database import connection

def InsertUser(usrName,usrLName,usrTel):
    cursorInsert = connection.cursor()

    query_insert = "CALL SP_NuevoUsuario ('"+usrName+"', '"+usrLName+"', '"+usrTel+"')"

    cursorInsert.execute(query_insert)
    connection.commit()