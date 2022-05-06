from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/camera')
def Camera():
    return render_template('camera.html')

@app.route('/templates/family')
def Family():
    return render_template('family.html')

@app.route('/recording')
def Recording():
    return render_template('recording.html')

if __name__ == '__main__':
    app.run(debug = True)