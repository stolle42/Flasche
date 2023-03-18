import flask
import werkzeug
from pathlib import Path
app=flask.Flask(__name__)

@app.route('/add')
def add():
    return flask.render_template("upload.html")

@app.route('/upload',methods=["POST"])
def upload():
    f=flask.request.files['newImg']
    location=Path.cwd()/"uploads"/f.filename
    location.parent.mkdir(parents=True, exist_ok=True)

    f.save(str(location))
    return f"file uploaded to {location}"


if __name__=="__main__":
    app.config['UPLOAD_FOLDER']=Path.cwd()/"sbook"/"uploads"
    app.run(host='localhost',port=5000, debug = True)
   