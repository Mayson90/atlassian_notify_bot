import requests
import json
from atlassian import Jira
from atlassian import Confluence


# Setup connection
username = '{{ USERNAME }}'
password = '{{ PASSWORD }}'
url_jira = '{{ JIRA_URL }}'
url_conf = '{{ CONF_URL }}'


jira = Jira(
    url=url_jira,
    username=username,
    password=password)

confluence = Confluence(
    url=url_conf,
    username=username,
    password=password)


def jira_license_info():
    url_api = url_jira + '/rest/plugins/applications/1.0/installed/jira-software'
    r = requests.get(url=url_api, auth=(username, password))
    data = json.loads(r.text)
    active_users = data['accessDetails']['activeUserCount']
    licensed_users = data['accessDetails']['licensedUserCount']
    remaining = licensed_users - active_users
    if remaining <= 10:
        return remaining


def conf_license_info():
    remaining = confluence.get_license_remaining()["count"]
    if remaining <= 10:
        return remaining
