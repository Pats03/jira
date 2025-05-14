import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the values from environment variables
email = os.getenv("EMAIL")
api_token = os.getenv("API_TOKEN")
domain = os.getenv("DOMAIN")

url = f"https://{domain}/rest/api/3/search"

params = {
    "jql": "issuekey=SCRUM-2",  # Or use project=SCRUM to get all project issues
    "maxResults": 5,
    "fields": "key,status,assignee,priority"
}

headers = {
    "Accept": "application/json"
}

auth = HTTPBasicAuth(email, api_token)

response = requests.get(url, headers=headers, params=params, auth=auth)

data = response.json()

if response.status_code != 200:
    print("Error:", response.status_code, data)
else:
    for issue in data.get("issues", []):
        key = issue["key"]
        status = issue["fields"]["status"]["name"]
        assignee = issue["fields"]["assignee"]["displayName"] if issue["fields"]["assignee"] else "Unassigned"
        priority = issue["fields"]["priority"]["name"] if issue["fields"].get("priority") else "None"

        print(f"Ticket ID: {key}")
        print(f"Status: {status}")
        print(f"Assignee: {assignee}")
        print(f"Priority: {priority}")
        print("-" * 40)
