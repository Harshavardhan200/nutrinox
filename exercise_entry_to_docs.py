import requests
from datetime import datetime
GENDER = 'male'
WEIGHT_KG = 70
HEIGHT_CM = 198.12
AGE = 19
APP_ID = 'fd63d6d4'
API_KEY = 'ea544c875b874a5e46f503a07ec0c1ca'
exercise_text = input("Tell me which exercise you did:")
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
authonication = {'Authorization': 'Bearer harshavardhan'}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
sheets = 'https://api.sheety.co/d9112476a4dd8a3c80c4438a401ac448/workoutTracking/sheet1'
sheet = 'https://api.sheety.co/d9112476a4dd8a3c80c4438a401ac448/workout/sheet1'
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
exercise1 = result['exercises'][0]['name'].title()
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']
sheet_in = {
    'sheet1': {
        'date': today_date,
        'time': now_time,
        'exercise': exercise1,
        'duration': duration,
        'calories': calories
    }
}
resp = requests.post(sheets, json=sheet_in, headers=authonication)
print(resp.json())