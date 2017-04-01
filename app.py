import flask
import os
import requests


app = flask.Flask(__name__)
__apikey__ = 'ab2396d1a7eb19b3bf5452a560714f0d' 
cidTrump = 'N00023864'
cidRyan = 'N00004357'
cidRob = 'N00005285'
cidSam = 'N00005244'
cid = ''
@app.route('/')
def hello():
    
    apiKey = 'http://opensecrets.org/api/?method=candSummary&cid='+ cidTrump + '&cycle=2016&apikey='+__apikey__
    r = requests.get(apiKey).content
    #passing in apiKey string to be used by index
    return flask.render_template("index.html",apiKey = r,cidTrump = cidTrump,
                                cidRyan = cidRyan, cidRob = cidRob, cidSam = cidSam) 

@app.route('/dez')
def dez():
    return flask.render_template('staywoke.html')

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP','0.0.0.0')
	)