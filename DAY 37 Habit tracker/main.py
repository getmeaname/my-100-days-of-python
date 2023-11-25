import requests
from datetime import datetime

# Create a user account.

USER_NAME = "xarunx"
USER_TOKEN = "ahufehfidjaihf"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": USER_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# Create your custom graph.

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
GRAPH_ID = "graph1"

graph_params = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "min",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": USER_TOKEN
}

# graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(graph_response.text)

# Post your progress.
POST_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}"
today = datetime.now()

post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many min have you spent on programming."),
}

post_response = requests.post(url=POST_ENDPOINT, json=post_params, headers=headers)
print(post_response.text)

# Update your progress.

update_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "24",
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Delete your progress.

delete_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# delete_response = requests.delete(url=delete_endpoint, headers=headers)
# print(delete_response.text)
