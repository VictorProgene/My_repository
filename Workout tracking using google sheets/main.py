import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 172
AGE = 27
API_Key = os.environ["API_Key"]
APP_ID = os.environ["APP_ID"]
API_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_text = input("What is the exercise? ")

credentials_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_Key,
}

REQUEST_BODY = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER,
}

response = requests.post(API_ENDPOINT, json=REQUEST_BODY, headers=credentials_header)
result = response.json()
print(result)


# --------------------------------GOOGLE SHEETS-----------------------------------------

SHEET_API_ENDPOINT = "https://api.sheety.co/20367f2872933ba1af4f10418c273a78/myWorkouts/workouts"
SHEET_TOKEN = os.environ["SHEET_TOKEN"]
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    headers = {
        "Authorization": f"Bearer {SHEET_TOKEN}",
    }

    sheet_response = requests.post(SHEET_API_ENDPOINT, json=sheet_inputs, headers=headers)
    print(sheet_response.text)