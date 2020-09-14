#!/usr/bin/python3
"""get information about his/her TODO list progress with CSV format"""
import csv
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
    FILE = str(USER_ID) + '.csv'
with open(FILE, mode='w') as f:
    csv = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for tasks in todo:
        TASK_COMPLETED_STATUS = tasks.get("completed")
        TASK_TITLE = tasks.get("title")
        csv.writerow([USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])
