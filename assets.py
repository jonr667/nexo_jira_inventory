from jira_requests import jira_requests
from item_management import item_management
import json
myitem = item_management()
myitem.test()
#myjson = myitem.list_catagories()
#print(myjson.json())
# myitem.add_item("type.tv", "Electronics/TV", "mytitle")
items = myitem.search_items("spartez.value", "2899.0")
print(items.json())
#print(type(items.text))
