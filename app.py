from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

app = Flask(__name__)

## Route for a home page

##@app.route('/')

def index():
    return 'Hello'     

if __name__=="__main__":
    app.run()        
