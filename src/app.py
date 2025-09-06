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
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], "123.jpg"))
        filename=os.path.join(app.config['UPLOAD_FOLDER'], "123.jpg")
        return render_template("index2.html", filename=filename)

@app.route('/fish')
def fish(filename): 
    return render_template("index2.html",filename=filename)

if __name__=="__main__":
    app.run(debug=True)