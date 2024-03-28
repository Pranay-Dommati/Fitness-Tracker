import requests
import os
from datetime import datetime
API_KEY = os.environ.get('API_KEY')
API_ID = os.environ['API_ID']
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_post_endpoint = YOUR_SHEETY_ENDPOINT
sheety_token = os.environ.get('SHEETY_TOKEN')
GENDER = "male"
WEIGHT_KG = 50
HEIGHT_CM = 170
AGE = 18
date = datetime.now().date()
time = datetime.now().strftime("%X")
headers = {
    'x-app-id':API_ID,
    'x-app-key':API_KEY
}
params = {
    "query":input("Enter what you did:"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=NUTRI_ENDPOINT,headers=headers,json=params)

data = response.json()['exercises']
formatted_data = [{"Exercise":value["name"],
                   "Duration":value["duration_min"],
                   "Calories":value["nf_calories"]} for value in data]
print(formatted_data)
headers_sheety ={
    'Content-Type': 'application/json',
    'Authorization': sheety_token
}
for _ in formatted_data:
    sheety_params = {
        "workout":{
            "date":f"{date}",
            "time":f"{time}",
            "exercise":_['Exercise'],
            "duration":_['Duration'],
            "calories":_['Calories']
        }
    }
    sheety_response = requests.post(url=sheety_post_endpoint,json=sheety_params,headers=headers_sheety)
    print(sheety_response.text)
    sheety_response.raise_for_status()







