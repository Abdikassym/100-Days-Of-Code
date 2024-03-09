import datetime

import requests
from datetime import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "abdesha"
TOKEN = "sndfpnagnajweasdlvlsajdnvopr"
graphID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": graphID,
    "name": "Running Habit Tracker",
    "unit": "kilometer",
    "type": "float",
    "color": "sora",
}

graph_headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}"
date_today = dt.today().strftime("%Y%m%d")
yesterday = (dt.today() - datetime.timedelta(1)).strftime("%Y%m%d")


post_graph_config = {
    "date": date_today,
    "quantity": "1"
}

# response = requests.post(url=pixel_creation_endpoint, json=post_graph_config, headers=graph_headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}/{yesterday}"


update_graph_config = {
    "quantity": "15",
}

# response = requests.put(url=pixel_update_endpoint, json=update_graph_config, headers=graph_headers)
# print(response.text)

pixel_delete_endpoint = pixel_update_endpoint

# response = requests.delete(url=pixel_delete_endpoint, headers=graph_headers)
# print(response.text)
