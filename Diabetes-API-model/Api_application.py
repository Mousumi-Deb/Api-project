
# load the libraries
import json
import requests

# Define the URL of the API endpoint
url = ' http://127.0.0.1:8000/diabetes_prediction_app'

# Define input data for the model.
# Define input data for the model.
input_model_data = {
    'Pregnancies': 6,
    'Glucose': 148,
    'BloodPressure': 72,
    'SkinThickness': 35,
    'Insulin': 0,
    'BMI': 33.6,
    'DiabetesPedigreeFunction': 0.627,
    'Age': 50
}


# Convert input data to JSON format
input_json = json.dumps(input_model_data)

# Make a POST request to the API endpoint with the input data
response = requests.post(url, data=input_json)

print(response.text)
