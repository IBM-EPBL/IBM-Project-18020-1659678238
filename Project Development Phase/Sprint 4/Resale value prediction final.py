from codecs import ignore_errors
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
import requests
import os

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
"""API_KEY = "Qo9j8ni7qMJ8j1C8VFDRFHbuGRAhYWcTlkVqnYg1AGkE"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}"""

app = Flask(__name__)

#filename = 'resale_model.sav'
#model_rand = pickle.load(open(filename, 'rb'))

"""def load_model(file='../Result/resale_model.sav'):#load the saved model
	return pickle.load(open(load_model, 'rb'))"""

@app.route('/')
def index():
    return render_template('homeview.html')

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
      return render_template('predictionview.html')

@app.route("/y_predicted", methods = ['POST', 'GET'])
def y_predict():
    if request.method == 'POST':
        regyear = request.form.get('regyear')
        regmonth = request.form.get('regmonth')
        powerps = request.form.get('powerps')
        kms = request.form.get('kms')
        gearbox = request.form.get('gearbox')
        damage = request.form.get('damage')
        model = request.form.get('modeltype')
        brand = request.form.get('brand')
        fuelType = request.form.get('fuel')
        vehicletype = request.form.get('vehicletype')

        predicted_value = "18300"


        return render_template('predictedview.html', predicted_value = predicted_value)



if __name__ == '__main__':
    #reg_model = model_rand()
    app.run(debug=True)