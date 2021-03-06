# -*- coding: utf-8 -*-
#==============================================================================
#
# TwiFreeze App
# Flask
# Twitter API
# Send Emails
#==============================================================================
# to see hello2.html (user entry form) on the browser (chrome):
# run hello.py in python (using terminal)
# thats it!
# make sure hello2.html is saved in templates in the same folder as hello.py

import os #added to deploy using heroku
from flask import Flask, request, render_template

app = Flask("MyApp")

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/signup", methods=['POST'])
def sign_up():
    form_data = request.form
    print form_data['hashtag']
    print form_data['email']
    print form_data['rawdata']

    os.system('Streamlistener.py'> rawdata.txt)
    os.system('Dataprocess.py')
    os.system('email_nomailgun.py')
    return render_template("allok.html")

#added bit to deploy using heroku
if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)
        
