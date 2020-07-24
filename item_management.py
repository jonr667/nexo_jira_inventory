from jira_requests import jira_requests


class item_management:
    def __init__(self):
        self.my_request = jira_requests()

    def add_item(self):
        json_dict = {'typeName': 'widget', 'categoryName': 'Widgets', 'fields': [{'typeName': 'system.title', 'values': ['myname2']}]}
        self.my_request.post_data("item", json_dict)

#r = requests.post('http://localhost:8088/rest/com-spartez-ephor/1.0/item', json={'typeName': 'widget', 'categoryName': 'Widgets', 'fields': [{'typeName': 'system.title', 'values': ['myname2']}]}, auth=HTTPBasicAuth('jringuette', 'mypassword'), headers=headers)

    def list_catagories(self):
        params_dict={'recursive': 'True'}
        returned_values = self.my_request.get_data("category", params_dict)
        # print(returned_values.json())
        return returned_values

    def find_item(self):
        pass

    def create_item_type(self):
        pass

    def update_item(self):
        pass

    def link_item_to_item(self):
        pass

    def link_item_to_issue(self):
        pass

    def link_issue_to_item(self):
        pass

    def test(self):
        print("Hello!, username is : %s, password is : %s" % (self.my_request.username, self.my_request.password))
