import requests
import datetime as dt

# CONSTANTS:
USERNAME = "koushiksdhu"
TOKEN = "s12fgdgsgdf121sdfg15sdf5df"

HEADERS = {
    "X-USER-TOKEN": TOKEN
}

# POST REQUEST METHOD:

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_PARAMETER = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# pixela_response = requests.post(
#     url=PIXELA_ENDPOINT, json=PIXELA_PARAMETER)
# print(pixela_response.text)


# CREATE A NEW GRAPH:

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_CONFIG = {
    "id": "graph1",
    "name": "Habit Graph",
    "unit": "commit",
    "type": "int",
    "color": "ichou"
}


# graph_response = requests.post(
#     url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADERS
# )
# print(graph_response.text)


# POSTING VALUE TO THE GRAPH:

GRAPH_POST = f"{GRAPH_ENDPOINT}/{GRAPH_CONFIG['id']}"
GRAPH_POST_PARAMETERS = {
    "date": str(dt.date.today().strftime("%Y%m%d")),
    "quantity": "5"
}

# graph_post_response = requests.post(
#     url=GRAPH_POST, json=GRAPH_POST_PARAMETERS, headers=HEADERS
# )
# print(graph_post_response.text)


# UPDATING USING PUT REQUEST:

UPDATE_ENDPOINT = f"{GRAPH_POST}/{dt.date.today().strftime('%Y%m%d')}"
UPDATE_PARAMETERS = {
    "quantity": "1"     # New data that is to be updated with.
}

# update_response = requests.put(
#     url=UPDATE_ENDPOINT, json=UPDATE_PARAMETERS, headers=HEADERS
# )
# print(update_response.text)


# DELETING USING DELETE REQUEST:

DELETE_ENDPOINT = f"{GRAPH_POST}/{dt.date.today().strftime('%Y%m%d')}"

delete_response = requests.delete(
    url=DELETE_ENDPOINT, headers=HEADERS
)
print(delete_response.text)
