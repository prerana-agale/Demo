import requests
from pprint import pprint

API_URL = "https://api.github.com"
GITHUB_TOKEN = "a5ab94921d269b12cef5004ed072409c898fd832"
headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}

def updaterepo():
    update_repo = requests.patch(API_URL + "/repos/preranaagale/PreranaAgale", data='{"name":"New Demo 1"}', headers=headers)
    pprint(update_repo.json())