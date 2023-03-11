import flask
# from calclib import get_mult
from flask import Flask, render_template, request, make_response

app=flask.Flask(__name__)

@app.route('/top')
def top():
   topscorer={"autist":152,"mongo":21,"omikronssohn":0}
   return flask.render_template("top.html",data=topscorer)
   

@app.route('/')
def startpage():
   print("all cookies:")
   print(flask.request.cookies)
   return flask.render_template("calc.html",level=flask.request.cookies.get('level'))

@app.route('/level')
def level():
   return flask.render_template("setlevel.html")

@app.route('/setcookie', methods = ['POST'])
def setcookie():
   response=flask.make_response( flask.redirect(flask.url_for("startpage")))
   response.set_cookie('level', request.form['level_form'])
   
   return response
   
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if flask.request.method == 'POST':
      user_answers = flask.request.form
      response=flask.make_response( flask.render_template("result.html",answers = user_answers,results={"m1":"161"}))
      response.set_cookie('level',user_answers["m1"])
      return response

if __name__=="__main__":
    app.run(host='localhost',port=5000, debug = True) #What does that mean? Set to ‘0.0.0.0’ to have server available externally