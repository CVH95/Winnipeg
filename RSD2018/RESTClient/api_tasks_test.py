#!/usr/bin/python

# MES API: TEST 1.0

import mes_api

print "REST API TEST 1.0"
print "\n"

# URL definition
_uri = 'http://localhost:3000/'
_path = 'tasks/'

# Add a new task to the list
ss1 = raw_input("Enter task name: ") #Dog
dd1 = raw_input("Enter task description: ") #Take the dog out for a walk
resp = mes_api.new_order(_uri, _path, ss1, dd1)                 # add task
if resp.status_code != 201:                                     # check status
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('New task added with ID: {}'.format(resp.json()["id"]))
print('Task summary: {}'.format(resp.json()["summary"]))
print "\n"

# Add a new task to the list
ss2 = raw_input("Enter task name: ")
dd2 = raw_input("Enter task description: ")
resp = mes_api.new_order(_uri, _path, ss1, dd1)                 # add task
if resp.status_code != 201:                                     # check status
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('New task added with ID: {}'.format(resp.json()["id"]))
print('Task summary: {}'.format(resp.json()["summary"]))
print "\n"

print "     >> Current task list:"
print "\n"

# Get all current tasks
resp = mes_api.get_orders(_uri, _path)
for todo_item in resp.json():
    print('Task ID: {}'.format(todo_item["id"]))
    print('Task summary: {}'.format(todo_item["summary"]))
    print('Full description: {}'.format(todo_item["description"]))
    print "\n"