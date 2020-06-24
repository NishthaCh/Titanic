# importing libraries
import pandas as pd
import numpy as np
import math
import json
from flask import Flask,request, render_template,jsonify
import pickle

# load model
rr=pickle.load(open('./Ridge_Titanic.pkl','rb'))

# app
app= Flask(__name__)

# routes
@app.route('/')
def homme():
    return render_template('UI_Titanic.html')

@app.route('/predict',methods=['POST'])
def my_prediction():
    try:
        # get data
        X = json.loads(request.form.get('X'))

        # predictions
        y_pred=rr.predict(X)
        z=math.exp(-y_pred)
        probability=1/(1+z)
        
        # send back to browser
        output = {'results': round(probability*100, 2)}

        # return data
        return jsonify(results=output)
    
    except Exception as e:
        print(e)
        return jsonify({'message':'Some error occured'}), 500

    
if __name__ == "__main__":
    app.run(port=5000,debug=True)   
    