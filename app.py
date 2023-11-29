from flask import Flask,request,render_template
import numpy as np
import pandas as pd


from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

app=Flask(__name__)

## app = Flask(application)

## Route for a home page

##@app.route('/')
##def index():
##    return render_template('index.html') 

# some bits of text for the page.

def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username
    
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'


# add a rule for the index page.
app.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))


if __name__=="__main__":
       app.run()
