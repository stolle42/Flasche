import flask
app=flask.Flask(__name__)


@app.route('/top')
def top():
   topscorer={"autist":152,"mongo":21,"omikronssohn":0}
   return flask.render_template("top.html",data=topscorer)
   

@app.route('/correct/<int:answer>')
def correct(answer):
    return flask.render_template("result.html",answer=answer,result=23*7)

@app.route('/',methods=['POST','GET'])
def startpage():
   if flask.request.method == 'POST':
      uc = flask.request.form['usercalc']
      return flask.redirect(flask.url_for('correct',answer = uc))
   else:
      uc = flask.request.args.get('usercalc')
      return flask.redirect(flask.url_for('correct', answer=uc))

if __name__=="__main__":
    app.run(host='localhost',port=5000, debug = True) #What does that mean? Set to ‘0.0.0.0’ to have server available externally