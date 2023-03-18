import flask

app=flask.Flask(__name__)
users=['admin','mongo','opfer','autist']

@app.route('/top')
def top():
   topscorer={"autist":152,"mongo":21,"omikronssohn":0}
   return flask.render_template("top.html",data=topscorer)
   

@app.route('/')
def startpage():
   print("all cookies:")
   print(flask.request.cookies)
   if "userIdx" in flask.session:
      level=flask.request.cookies.get('level')
      userIdx=flask.session.get('userIdx')
      return flask.render_template("calc.html",level=level,username=users[userIdx])
   else:
      msg=flask.get_flashed_messages()
      return flask.render_template("notloggedin.html",message=msg[0] if msg else "Welcome!")

@app.route('/login',methods=['GET','POST'])
def login():
      if flask.request.method=='POST':
         uname=flask.request.form['formForUsername']
         if uname in users:
            flask.session['userIdx']=users.index(uname)
            return flask.redirect(flask.url_for("startpage"))
         else: 
            flask.abort(401)
      else:
         return flask.render_template("login.html",)
   
@app.route('/signup')
def signup():
   return flask.abort(501)
   
@app.route('/logout')
def logout():
   flask.flash("You logged out sucessfuly!")
   flask.session.pop('userIdx')
   return flask.redirect(flask.url_for("startpage"))
   
# getFlashMessage(idx):
#    ree
   
   
@app.route('/level')
def level():
   return flask.render_template("setlevel.html")

@app.route('/setcookie', methods = ['POST'])
def setcookie():
   response=flask.make_response( flask.redirect(flask.url_for("startpage")))
   response.set_cookie('level', flask.request.form['level_form'])
   
   return response
   
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if flask.request.method == 'POST' and flask.session['userIdx']: #do not allow result view when not logged in
      user_answers = flask.request.form
      response=flask.make_response( flask.render_template("result.html",answers = user_answers,results={"m1":"161"}))
      response.set_cookie('level',user_answers["m1"])
      return response
   else:
      flask.abort(401)

if __name__=="__main__":
   app.secret_key='your_secret_key'
   app.config['SESSION_COOKIE_NAME'] = 'your_session_cookie_name'
   app.config['SESSION_COOKIE_SECURE'] = True  # only send session cookies over HTTPS
   app.config['SESSION_COOKIE_HTTPONLY'] = True  # prevent JavaScript from accessing session cookies
   app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # protect against cross-site request forgery (CSRF) attacks
   app.config['SESSION_COOKIE_LIFETIME'] = None
   app.run(host='localhost',port=5000, debug = True)