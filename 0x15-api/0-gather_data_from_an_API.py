#!/usr/bin/python3
"""get information about his/her TODO list progress"""
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
        EMPLOYEE_NAME = usr.get('name')
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = ""
    for tasks in todo:
        if tasks.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE += "\t " + tasks["title"] + "\n"
    print("Employee {} is done with tasks({}/{}):".
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, len(todo)))
    print("{}".format(TASK_TITLE)[:-1])
