#!/usr/bin/python3
"""get information about his/her TODO list progress with JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/",
                         params={"userId": argv[1]})
    users = requests.get("https://jsonplaceholder.typicode.com/users/",
                         params={"id": argv[1]})
    todo = todos.json()
    user = users.json()

    for usr in user:
        USERNAME = usr.get('username')
        USER_ID = usr.get('id')
    FILE = str(USER_ID) + '.json'
    data = {USER_ID: []}
    with open(FILE, mode='w') as f:
        for tasks in todo:
            new_dic = {}
            new_dic["task"] = tasks.get('title')
            new_dic["completed"] = tasks.get('completed')
            new_dic["username"] = USERNAME
            data[USER_ID].append(new_dic)
        json.dump(data, f)
