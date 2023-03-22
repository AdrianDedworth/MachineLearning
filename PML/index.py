import time
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, flash, Response
import os
from src.CheckExtension import allowed_file
from src.InsertUser import InsertUser
from src.GetID import GetID
from src.Entrenamiento import TrainingSystem
from src.capture import CaptureFace
from src.videoStreaming import videoStreaming

app = Flask(__name__, template_folder='templates')
app.config["UPLOAD_FOLDER"] = "static/uploads/"
app.secret_key = 'rtxz'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/videoStream')
def videoStream():
    return Response(videoStreaming(), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route('/family')
def family():
    return render_template('family.html')

@app.route('/upload', methods=["POST", "GET"])
def upload():
    file = request.files["uploadFile"]
    #print(file, file.filename)
    filename = secure_filename(file.filename)
    #print(filename)

    # Creating folder to save the video
    usrID = GetID() + 1
    pathToSave = os.path.join(app.config["UPLOAD_FOLDER"], str(usrID))

    usrName = request.form['fname']
    usrLName = request.form['lname']
    usrTel = request.form['num-cel']

    if not os.path.exists(pathToSave):
        #print("carpeta creada: " + pathToSave)
        os.mkdir(pathToSave)
        facesFolder = pathToSave + '/rostros'
        os.mkdir(facesFolder)

    if file and allowed_file(filename):
        #print("Video guardado")
        file.save(os.path.join(pathToSave, filename))
        flash("Datos guardados. Video subido y listo para iniciar entrenamiento", "success")
        #inserta nuevo usuario
        InsertUser(usrName, usrLName, usrTel)

        #cambio de nombre del archivo de video para facilitar su uso
        extension = filename.split('.')
        newVideoName = str(usrID) + '.' + extension[1]
        destination = pathToSave + '/' + newVideoName
        source = os.path.join(pathToSave, filename)
        os.rename(source, destination)

        return render_template('family.html', entrenaStatus = "active")
    else:
        #print("video con formato invalido")
        flash("Datos no guardados.\nVideo con formato invalido. Formatos aceptados: mp4, avi, mpg o wmv", "danger")
        return render_template('family.html', name = usrName, lname = usrLName, telef = usrTel)

@app.route('/entrena')
def entrena():
    CaptureFace()
    time.sleep(1)
    message = TrainingSystem()
    return render_template('family.html', trainingText = message, entrenaStatus = "")

@app.route('/recording')
def recording():
    return render_template('recording.html')

if __name__ == '__main__':
    app.run(debug = True)