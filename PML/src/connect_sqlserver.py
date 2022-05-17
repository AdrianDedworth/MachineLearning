import pyodbc

try:
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1,1433;DATABASE=dbMachineLearning;UID=sa;PWD=S3rv3r')
    print("Conexión Exitosa")
except Exception as ex:
    print(ex)