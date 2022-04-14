#!/usr/bin/python3
"""gathers data from an API"""


if __name__ == "__main__":
    import requests
    import sys

    user_req = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                            format(sys.argv[1]))
    user_name = user_req.json().get("name")
    tasks_req = requests.get("https://jsonplaceholder.typicode.com/todos")
    total_tasks = 0
    cmp_tasks = 0
    cmp_tasks_desc = ""
    for each in tasks_req.json():
        if each["userId"] == int(sys.argv[1]):
            total_tasks += 1
            if each["completed"] is True:
                cmp_tasks += 1
                cmp_tasks_desc += "\t {}\n".format(each["title"])
    print("Employee {} is done with tasks({}/{}):".
          format(user_name, cmp_tasks, total_tasks))
    print(cmp_tasks_desc, end="")
