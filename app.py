import flask
import os
import requests


app = flask.Flask(__name__)
cid = ''
@app.route('/')
def hello():
    __apikey__ = 'ab2396d1a7eb19b3bf5452a560714f0d' 
    cidTrump = 'N00023864'
    cidRyan = 'N00004357'
    cidRob = 'N00005285'
    cidSam = 'N00005244'

      #passing in apiKey string to be used by html files
    
    apiKey = 'http://opensecrets.org/api/?method=candSummary&cid='+ cidTrump + '&cycle=2016&apikey='+__apikey__
    r = requests.get(apiKey).content
    cidTrumpv = requests.get('http://opensecrets.org/api/?method=candSummary&cid='+ cidTrump + '&cycle=2016&apikey='+__apikey__)
    cidRyanv = requests.get('http://opensecrets.org/api/?method=candSummary&cid='+ cidRyan + '&cycle=2016&apikey='+__apikey__)
    cidRobv = requests.get('http://opensecrets.org/api/?method=candSummary&cid='+ cidRob + '&cycle=2016&apikey='+__apikey__)
    cidSamv = requests.get('http://opensecrets.org/api/?method=candSummary&cid='+ cidSam + '&cycle=2016&apikey='+__apikey__)
  
    #Top Contributors to particular candidates
    contriTrump = requests.get('http://www.opensecrets.org/api/?method=candContrib&cid=' + cidTrump '&cycle=2016&apikey='__apikey__)
    contriRyan = requests.get('http://www.opensecrets.org/api/?method=candContrib&cid=' + cidRyan '&cycle=2016&apikey='__apikey__)
    contriRob = requests.get('http://www.opensecrets.org/api/?method=candContrib&cid=' + cidRob '&cycle=2016&apikey='__apikey__) 
    contriSam = requests.get('http://www.opensecrets.org/api/?method=candContrib&cid=' + cidSam '&cycle=2016&apikey='__apikey__)
    
   #getting industry content for politicians
   indTrump = requests.get('http://www.opensecrets.org/api/?method=candIndustry&cid='+ cidTrump +'&cycle=2016&apikey=__apikey__') 
   indRyan = requests.get('http://www.opensecrets.org/api/?method=candIndustry&cid='+ cidRyan +'&cycle=2016&apikey=__apikey__')
   indRob = requests.get('http://www.opensecrets.org/api/?method=candIndustry&cid='+ cidRob +'&cycle=2016&apikey=__apikey__')
   indSam = requests.get('http://www.opensecrets.org/api/?method=candIndustry&cid='+ cidSam +'&cycle=2016&apikey=__apikey__')
   
   #getting sector data
   secTrump = requests.get('http://www.opensecrets.org/api/?method=candSector&cid=' + cidTrump + '&cycle=2012&apikey=__apikey__')
   secRyan = requests.get('http://www.opensecrets.org/api/?method=candSector&cid=' + cidRyan + '&cycle=2012&apikey=__apikey__')
   secRob =  requests.get('http://www.opensecrets.org/api/?method=candSector&cid=' + cidRob + '&cycle=2012&apikey=__apikey__')
   secSam =  requests.get('http://www.opensecrets.org/api/?method=candSector&cid=' + cidSam + '&cycle=2012&apikey=__apikey__')


)
    return flask.render_template("index.html", apiKey = r, cidTrump = cidTrumpv.content,
                                cidRyan = cidRyanv.content, cidRob = cidRobv.content,
                                cidSam = cidSamv.content, contriTrump = contriTrump.content,
                                contriRyan = contriRyan.content, contriRob = contriRob.content,
                                contriSam = contriSam.content, indTrump = indTrump.content,indRyan=indRyan.content,
                                indRob = indRob.content, indSam = indSam.content, secTrump = secTrump.content, 
                                secRyan=secRyan.content,secRob = secRob.content, secSam =secSam.content) 
                                

@app.route('/dez')
def dez():
    return flask.render_template('staywoke.html')

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP','0.0.0.0')
	)