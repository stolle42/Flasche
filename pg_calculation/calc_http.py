import flask
app=flask.Flask(__name__)


@app.route('/top')
def top():
   topscorer={"autist":152,"mongo":21,"omikronssohn":0}
   return flask.render_template("top.html",data=topscorer)
   

@app.route('/')
def startpage():
   return flask.render_template("calc.html")
   
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if flask.request.method == 'POST':
      user_answers = flask.request.form
      #TODO: add a1!!!! and remove that ugly "161"
      return flask.render_template("result.html",answers = user_answers,results={"m1":"161"})

if __name__=="__main__":
    app.run(host='localhost',port=5000, debug = True) #What does that mean? Set to ‘0.0.0.0’ to have server available externally