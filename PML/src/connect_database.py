import pymysql

host = 'bkolugnb8jl7o13ohycl-mysql.services.clever-cloud.com'
port = '3306'
database = 'bkolugnb8jl7o13ohycl'
user = 'umsrhsmzuxb6yc6c'
password = 'RZRdT0Iec1yI6ePgNZjK'

try:
    connection = pymysql.connect(host=host, user=user, password=password, db=database, cursorclass=pymysql.cursors.DictCursor)
    print("Conexión Exitosa")
except Exception as ex:
    print(ex)