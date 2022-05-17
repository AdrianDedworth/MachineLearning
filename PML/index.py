from colorama import Cursor
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, flash
import os
from src.connect_sqlserver import connection

app = Flask(__name__, template_folder='templates')
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.secret_key = 'rtxz'
ALLOWED_EXTENSIONS = set(['mp4', "avi", "wmv", "mpg"])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/family')
def family():
    cursorGetID = connection.cursor()

    high_ID = "SELECT  TOP 1 IDUsuario from tblUsuario ORDER BY IDUsuario DESC"
    cursorGetID.execute(high_ID)

    usrID = cursorGetID.fetchval()

    usrID += 1
    return render_template('family.html', ID_usuario = usrID)

def allowed_file(file):
    file = file.split('.')
    if file[1].lower() in ALLOWED_EXTENSIONS:
        return True
    return False

@app.route('/upload', methods=["POST", "GET"])
def upload():
    file = request.files["uploadFile"]
    print(file, file.filename)
    filename = secure_filename(file.filename)
    print(filename)

    # Creating folder to save the video
    usrID = request.form['idfam']
    pathToSave = os.path.join(app.config["UPLOAD_FOLDER"], usrID)

    usrName = request.form['fname']
    usrLName = request.form['lname']
    usrTel = request.form['num-cel']

    if not os.path.exists(pathToSave):
        print("carpeta creada: " + pathToSave)
        os.mkdir(pathToSave)

    if file and allowed_file(filename):
        print("Video guardado")
        archivoEstado = 1
        file.save(os.path.join(pathToSave, filename))
    else:
        archivoEstado = 0

    if archivoEstado == 1:
        flash("Video subido y listo para iniciar entrenamiento", "success")
        #inserta nuevo usuario
        cursorInsert = connection.cursor()
        columns = "INSERT INTO tblUsuario(Usuario_Nombre, Usuario_Apellido, Usuario_Telef, Usuario_Estado)"
        newData = " VALUES ('"+usrName+"', '"+usrLName+"', '"+usrTel+"', 1)"

        query_insert = columns + newData

        cursorInsert.execute(query_insert)
        connection.commit()

        return render_template('home.html')
    elif archivoEstado == 0:
        print("video con formato invalido")
        flash("Datos no guardados...\nvideo con formato invalido... Formatos aceptados: mp4, avi, mpg o wmv", "danger")
        return render_template('family.html', name = usrName, lname = usrLName, telef = usrTel)

@app.route('/recording')
def recording():
    return render_template('recording.html')

if __name__ == '__main__':
    app.run(debug = True)