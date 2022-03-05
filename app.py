from flask import Flask, escape, request, render_template
import os
from werkzeug.utils import secure_filename
import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = params['upload_location']

@app.route('/')
def uplaod_image():
    return render_template("index1.html")

@app.route("/upload" , methods=['GET', 'POST'])
def uploader():
    if request.method=='POST':
        f = request.files['file1']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        ff=os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        return fish()

@app.route('/fish')
def fish():
    return render_template("index2.html")

if __name__=="__main__":
    app.run(debug=True)