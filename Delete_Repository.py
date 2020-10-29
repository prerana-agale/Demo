import requests
from pprint import pprint
from secret import Token_Value

API_URL = "https://api.github.com"
GITHUB_TOKEN = "a5ab94921d269b12cef5004ed072409c898fd832"
headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}


def deleterepo():
    delete_repo = requests.delete(API_URL + "/repos/preranaagale/Demo", headers=headers)
    pprint(delete_repo.text)