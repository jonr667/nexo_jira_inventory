import requests, json
from requests.auth import HTTPBasicAuth

# Class for making requests to JIRA w/ Asset tracker addon, post and get calls and reads username/password from jira_creds.txt
class jira_requests:

    def __init__(self, username="", password="", password_file="jira_creds.txt"):
        self.asset_tracker_url = 'http://45.56.82.161:8080/rest/com-spartez-ephor/1.0/'
        self.headers={'Content-type': 'application/json', 'Accept': 'application/json'}
        self.username = username
        self.password = password
        if username or password == "":
            self.username, self.password = self.read_username_password_from_file(password_file)

    def post_data(self, operator, json_string):
        request_url = self.asset_tracker_url + operator
        returned_value = requests.post(request_url, json=json_string, auth=HTTPBasicAuth(self.username, self.password, headers=self.headers))
        return returned_value

    def get_data(self, operator, params_dict=''):
        request_url = self.asset_tracker_url + operator
        returned_value = requests.get(request_url, params=params_dict, auth=HTTPBasicAuth(self.username, self.password))
        return returned_value

    def read_username_password_from_file(self, password_file):
        username = ""
        password = ""
        try:
            with open(password_file) as userpass_file:
                username, password = userpass_file.readline().rstrip().split(':')
        except IOError:
            print("Could not open password file. ()")
            return -1
        return username, password