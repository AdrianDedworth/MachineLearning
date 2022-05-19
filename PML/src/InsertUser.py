from src.connect_sqlserver import connection

def InsertUser(usrName,usrLName,usrTel):
    cursorInsert = connection.cursor()

    query_insert = "EXEC SP_NuevoUsuario '"+usrName+"', '"+usrLName+"', '"+usrTel+"'"

    cursorInsert.execute(query_insert)
    connection.commit()