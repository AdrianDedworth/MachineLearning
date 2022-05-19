from src.connect_sqlserver import connection

def NewID():
    cursorGetID = connection.cursor()

    highest_ID = "EXEC SP_GetHighestID"
    cursorGetID.execute(highest_ID)

    usrID = cursorGetID.fetchval()
    usrID += 1
    return usrID