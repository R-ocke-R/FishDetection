from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return render_template("index.html")
    # return f'Hello, {escape(name)}!'

if __name__=="__main__":
    app.run(debug=True)