from colorama import Cursor
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, flash
import os
from src.CheckExtension import allowed_file
from src.InsertUser import InsertUser
from src.NewID import NewID
#from static.capture import CaptureFaces

app = Flask(__name__, template_folder='templates')
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.secret_key = 'rtxz'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/family')
def family():
    usrID = NewID()
    return render_template('family.html', ID_usuario = usrID)

@app.route('/upload', methods=["POST", "GET"])
def upload():
    file = request.files["uploadFile"]
    #print(file, file.filename)
    filename = secure_filename(file.filename)
    #print(filename)

    # Creating folder to save the video
    usrID = request.form['idfam']
    pathToSave = os.path.join(app.config["UPLOAD_FOLDER"], usrID)

    usrName = request.form['fname']
    usrLName = request.form['lname']
    usrTel = request.form['num-cel']

    if not os.path.exists(pathToSave):
        #print("carpeta creada: " + pathToSave)
        os.mkdir(pathToSave)

    if file and allowed_file(filename):
        #print("Video guardado")
        file.save(os.path.join(pathToSave, filename))
        flash("Datos guardados. Video subido y listo para iniciar entrenamiento", "success")
        #inserta nuevo usuario
        InsertUser(usrName, usrLName, usrTel)
        usrID = NewID()
        return render_template('family.html', ID_usuario = usrID)
    else:
        #print("video con formato invalido")
        flash("Datos no guardados.\nVideo con formato invalido. Formatos aceptados: mp4, avi, mpg o wmv", "danger")
        return render_template('family.html', name = usrName, lname = usrLName, telef = usrTel)

# @app.route('/entrena', methods=["POST", "GET"])
# def entrena():
#     videoPath = request.path['entrena']
#     CaptureFaces(videoPath)

@app.route('/recording')
def recording():
    return render_template('recording.html')

if __name__ == '__main__':
    app.run(debug = True)