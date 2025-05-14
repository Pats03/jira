# 🧾 Jira Issue Fetcher

A simple Python script to retrieve Jira issues using the Jira Cloud REST API. It demonstrates how to authenticate with Jira using email and API token, perform JQL-based issue queries, and display key issue details such as status, assignee, and priority.

## 📌 Features

- Connects securely to your Jira Cloud instance using environment variables
- Queries specific issues via JQL
- Fetches fields like:
  - Issue Key
  - Status
  - Assignee
  - Priority
- Prints formatted output to the console

## 🧰 Technologies Used

- Python 3.x
- `requests` for HTTP calls
- `python-dotenv` to manage environment variables securely
- Jira Cloud REST API v3

## 📂 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/jira-issue-fetcher.git
cd jira-issue-fetcher
pip install requests python-dotenv
EMAIL=your-email@example.com
API_TOKEN=your-jira-api-token
DOMAIN=your-domain.atlassian.net
python fetch_issues.py


Ticket ID: SCRUM-2
Status: In Progress
Assignee: John Doe
Priority: High
----------------------------------------
