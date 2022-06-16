from src.connect_database import connection

def SaveModel(modelName, modelPath):
    cursorInsert = connection.cursor()

    query_saveModel = "CALL SP_SaveModel ('"+modelName+"', '"+modelPath+"')"

    cursorInsert.execute(query_saveModel)
    connection.commit()
