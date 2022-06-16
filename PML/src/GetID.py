from src.connect_database import connection

def GetID():
    cursorGetID = connection.cursor()

    highest_ID = "CALL SP_GetHighestID"
    cursorGetID.execute(highest_ID)

    usrID = cursorGetID.fetchone()
    usrID = usrID.get('IDUsuario')
    return usrID