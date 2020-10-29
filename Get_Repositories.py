import requests
from pprint import pprint

API_URL = "https://api.github.com"
GITHUB_TOKEN = "a5ab94921d269b12cef5004ed072409c898fd832"
headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}

def getrepos():
    get_repos = requests.get(API_URL + "/user/repos", headers=headers)
    pprint(get_repos.json())