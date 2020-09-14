#!/usr/bin/python3
"""get information all TODO list progress with JSON format"""
import json
import requests



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
        data = {USER_ID: []}
        for tasks in todo:
            new_dic = {}
            new_dic["task"] = tasks.get('title')
            new_dic["completed"] = tasks.get('completed')
            new_dic["username"] = USERNAME
            data[USER_ID].append(new_dic)
        all_todo[user_id].append(data)
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(all_todo, f)
