
# load the libraries
from fastapi import FastAPI
from pydantic import BaseModel

import pickle
import json

# load the insistance of FastAPI
app = FastAPI()


class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiavetesPredigreeFunction: float
    Age: int

# load the saved diabetes model


diabetes_model = pickle.load(open('diabetic_model.sav', 'rb'))

# create a API model


@app.post('/Diabetes_prediction_app')
def diabetes_prediction(input_parameters: model_input):
    input_data = input_parameters
    input_dict = json.loads(input_data)

    preg = input_dict['pregnancies']
    glu = input_dict['Glucose']
    bp = input_dict['BloodPressure']
    skin = input_dict['SkinThickness']
    insulin = input_dict['Insulin']
    bmi = input_dict['BMI']
    dpf = input_dict['DiabetesPedigreeFunction']
    age = input_dict['Age']

    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]

    prediction = diabetes_model.predict([input_list])

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
