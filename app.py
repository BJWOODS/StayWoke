import flask
import os
import requests


app = flask.Flask(__name__)
__apikey__ = 'ab2396d1a7eb19b3bf5452a560714f0d' 
cid = 'N00000019'
@app.route('/')
def hello():
    
    apiKey = 'http://opensecrets.org/api/?method=candSummary&cid='+ cid + '&cycle=2012&apikey='+__apikey__
    r = requests.get(apiKey).content
    
    return flask.render_template("index.html",apiKey = r,cid = cid) #passing in apiKey string to be used by index

@app.route('/dez')
def dez():
    return flask.render_template('staywoke.html')

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP','0.0.0.0')
	)