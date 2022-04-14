#!/usr/bin/python3
"""
Gathers data from an API (for a single employee)
and exports it to JSON file
Format: { "USER_ID": [{"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS,"username": "USERNAME"},
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"},
    ... ]}
File name must be: USER_ID.json
"""


if __name__ == "__main__":
    import requests
    import sys
    import json

    user_req = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                            format(sys.argv[1]))
    user_name = user_req.json().get("username")
    user_id = user_req.json().get("id")
    tasks_req = requests.get("https://jsonplaceholder.typicode.com/todos")
    file_json = str(user_id) + ".json"
    json_data = {}
    value_list = []
    for each in tasks_req.json():
        if each["userId"] == int(sys.argv[1]):
            each.update([("username", user_name)])
            each.pop("id")
            each.pop("userId")
            each.update([("task", each["title"])])
            each.pop("title")
            value_list.append(each)
    json_data[user_id] = value_list

    with open(file_json, 'w', encoding='utf=8') as file:
        json.dump(json_data, file, indent=4)
