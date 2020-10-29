import requests
from pprint import pprint

API_URL = "https://api.github.com"
GITHUB_TOKEN = "a5ab94921d269b12cef5004ed072409c898fd832"
headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}
def getprojects():
    get_projects = requests.get(API_URL + "/users/preranaagale/projects", headers=headers)
    pprint(get_projects.json())