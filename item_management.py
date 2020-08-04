from jira_requests import jira_requests


class item_management:
    def __init__(self):
        self.my_request = jira_requests()

    def add_item(self, item_type, category, title):
        json_dict = {'typeName': item_type,
                     'categoryName': category,
                     'fields': [
                                {'typeName': 'system.title', 'values': [title]}
                                ]
                    }
        inserted_item = self.my_request.post_data("item", json_dict)
        return inserted_item

    def list_catagories(self):
        params_dict = {'recursive': 'True'}
        catagories = self.my_request.get_data("category", params_dict)
        return catagories

    def search_items(self, field, search_text):
        item_query = field + '=' + search_text
        params_dict = {'query': item_query}
        items = self.my_request.get_data("search", params_dict)
        return items

    def search_item_title(self, title):
        title_query = 'system.title=' + title
        params_dict = {'query': title_query}
        item = self.my_request.get_data("search", params_dict)
        return item

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

    def part_id_from_dict(self):
        pass

    def test(self):
        print("Hello!, username is : %s, password is : %s" % (self.my_request.username, self.my_request.password))
