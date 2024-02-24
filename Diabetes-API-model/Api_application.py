
# load the libraries
import json
import requests

# Define the URL of the API endpoint
url = 'http://127.0.0.1:8000/Diabetes_prediction_app'

# Define input data for the model.
input_model_data = {
    'pregnancies': 5,
    'Glucose': 166,
    'BloodPressure': 72,
    'SkinThickness': 19,
    'Insulin': 175,
    'BMI': 25.8,
    'DiabetesPedigreeFunction': 0.587,
    'Age': 51
}

# Convert input data to JSON format
input_json = json.dumps(input_model_data)

# Make a POST request to the API endpoint with the input data
response = requests.post(url, data=input_json)

print(response.txt)
