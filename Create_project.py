import requests
from pprint import pprint
from secret import Token_Value

API_URL = "https://api.github.com"
GITHUB_TOKEN = Token_Value
headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}
def createproject():
    create_project = requests.post(API_URL + "/user/projects", data='{"name":"Prerana A"}', headers=headers)
    pprint(create_project.json())
