#!/usr/bin/python3
"""get information all TODO list progress with JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    all_todo = {}
    for user in users:
        user_id = user["id"]
        todos = requests.get("https://jsonplaceholder.typicode.com/todos/",
                             params={"userId": user_id})
        users = requests.get("https://jsonplaceholder.typicode.com/users/",
                             params={"id": user_id})
        todo = todos.json()
        user = users.json()

        all_todo[user_id] = []
        for usr in user:
            USERNAME = usr.get('username')
            USER_ID = usr.get('id')
        for tasks in todo:
            data = {}
            data["task"] = tasks.get('title')
            data["completed"] = tasks.get('completed')
            data["username"] = USERNAME
        all_todo[user_id].append(data)
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(all_todo, f)
