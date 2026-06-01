#Get = request
#Post = give info
#Put = update info
#Delete = delete

import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "your pixela token"
USER_NAME = "your pixela user"
GRAPH_ID = "your graph ID"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# --------------------------------CREATE USER--------------------------

# Only use one time to create user
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# --------------------------------CREATE GRAPHIC-----------------------

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = { #THIS HIDE AND MAKE YOUR USER SECURE
    "X-USER-TOKEN": TOKEN,
}



# Only for graph creation
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)


# FOR CREATING PIXEL
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()#Y=If u want to use today's date
# today = datetime(year=2026, month=4, day=8) #If u need to create a pixel for past days, insert inside parentheses the date

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cicle today? "),
}

# To create a pixel
response = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)
print(response.text)

new_date = datetime(year=2026, month=4, day=9)

new_date_pixel_params = {
    "quantity": "40",
}

UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{new_date.strftime('%Y%m%d')}"

# Used for updating pixel value
# response = requests.put(UPDATE_PIXEL_ENDPOINT,  json=new_date_pixel_params, headers=headers)
# print(response.text)

DELETE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{new_date.strftime('%Y%m%d')}"

# Used for deleting pixel
# response = requests.delete(DELETE_PIXEL_ENDPOINT, headers=headers)
# print(response.text)










