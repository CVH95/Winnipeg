#!/usr/bin/python
import requests

# CREATE GET REQUEST
resp = requests.get('http://localhost:3000/tasks/') # remember using HTTP and NOT!!!!!!! https

# On success, status code is 200
if resp.status_code != 200:     # This means something went wrong.    
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

# Print list of 'to do' items IDs and summaries.
for todo_item in resp.json():
    #print('{} {}'.format(todo_item['id'], todo_item['summary']))
    print('Task ID: {}'.format(todo_item["id"]))
    print('Task summary: {}'.format(todo_item["summary"]))
    print('Full description: {}'.format(todo_item["description"]))