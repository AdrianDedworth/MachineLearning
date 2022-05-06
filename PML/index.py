from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='templates')
app.config["UPLOAD_FOLDER"] = "static/uploads"
ALLOWED_EXTENSIONS = set(['png', "jpg", "jpeg"])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/family')
def family():
    return render_template('family.html')

def allowed_file(file):
    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False

@app.route('/upload', methods=["POST"])
def upload():
    file = request.files["uploadFile"]
    print(file, file.filename)
    filename = secure_filename(file.filename)
    print(filename)
    if file and allowed_file(filename):
        print("permitido")
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    return 'A'

@app.route('/recording')
def recording():
    return render_template('recording.html')

if __name__ == '__main__':
    app.run(debug = True)