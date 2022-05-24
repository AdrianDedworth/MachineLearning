from src.connect_sqlserver import connection

def GetID():
    cursorGetID = connection.cursor()

    highest_ID = "EXEC SP_GetHighestID"
    cursorGetID.execute(highest_ID)

    usrID = cursorGetID.fetchval()
    return usrID