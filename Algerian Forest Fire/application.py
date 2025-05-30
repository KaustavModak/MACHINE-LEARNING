from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application

# importing ridge regressor and standard scaler
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Temperature=float(request.form['Temperature'])
        RH=float(request.form['RH'])
        Ws=float(request.form['Ws'])
        Rain=float(request.form['Rain'])
        FFMC=float(request.form['FFMC'])
        DMC=float(request.form['DMC'])
        ISI=float(request.form['ISI'])
        Classes=float(request.form['Classes'])
        Region=float(request.form['Region'])

        new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])

        result=ridge_model.predict(new_data_scaled)

        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)