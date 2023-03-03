import flask
app=flask.Flask(__name__)

rich=1e6
@app.route('/rich/<missing>')
def hellorich(missing):
    return "You are rich!"

@app.route('/poor/<int:missing>')
def hellopoor(missing):
    return f"Sorry, your poor! You're ${missing} short of being rich!"

@app.route('/salary/<int:salary>')
def hellouser(salary):
    state="hellopoor" if salary<rich else "hellorich"
    return flask.redirect(flask.url_for(state,missing=rich-salary))
    

if __name__=="__main__":
    app.run(host='localhost',port=5000, debug = True) #What does that mean? Set to ‘0.0.0.0’ to have server available externally