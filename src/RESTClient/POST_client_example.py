#!/usr/bin/python
import requests

# Dictionary for the task
task = {"summary": "Coffee", "description": "Make some coffee" }

# POST new task
resp = requests.post('http://localhost:3000/tasks/', json=task)

# On success, status code is 201
if resp.status_code != 201:
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))

# Print created task credentials
print('New task added with ID: {}'.format(resp.json()["id"]))
print('Task summary: {}'.format(resp.json()["summary"]))