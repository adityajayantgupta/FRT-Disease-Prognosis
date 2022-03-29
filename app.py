import numpy as np
from scipy.stats import mode
import pickle
from flask import Flask
from flask import request


app = Flask(__name__)

with open('svm_model.pkl', 'rb') as fid:
    final_svm_model = pickle.load(fid)
with open('nb_model.pkl', 'rb') as fid:
    final_nb_model = pickle.load(fid)
with open('rf_model.pkl', 'rb') as fid:
    final_rf_model = pickle.load(fid)
with open('data_dict.pkl', 'rb') as fid:
    data_dict = pickle.load(fid)

# Defining the Function
# Input: string containing symptoms separated by commmas
# Output: Generated predictions by models

@app.route('/')
def predictDisease():
    symptoms = request.args.get('symptoms')
    symptoms = symptoms.split(",")
     
    # creating input data for the models
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1
         
    # reshaping the input data and converting it
    # into suitable format for model predictions
    input_data = np.array(input_data).reshape(1,-1)
     
    # generating individual outputs
    rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(input_data)[0]]
    nb_prediction = data_dict["predictions_classes"][final_nb_model.predict(input_data)[0]]
    svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(input_data)[0]]
     
    # making final prediction by taking mode of all predictions
    final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])[0][0]
    predictions = {
        "rf_model_prediction": rf_prediction,
        "naive_bayes_prediction": nb_prediction,
        "svm_model_prediction": nb_prediction,
        "final_prediction":final_prediction
    }
    return predictions

