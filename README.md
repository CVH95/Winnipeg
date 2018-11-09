# REST API for the MES system.

## 1. Project Description.

 - **JSON Server:**

 Installing a basic JSON localhost server for development and trials (tasks.json).

 - **REST Client:**

    - POST and GET method examples with Python.
    - MES API example in Python.
    - Application of the API to interact with the server with (api\_tasks_test.py)

## 2. Setting up.

1.1. To install json sever for trials:

```sh
$ sudo apt install npm
$ sudo npm n -g
$ n latest
```
1.2. Create and run the server (server file used for trials: tasks.json):

```sh
$ gedit server.json < (fill it with watever stuff) >
$ json-server --watch server.json
```

1.3.Verify it is working by browsing http://localhost:3000/ and clicking on the tab **_tasks_**.

1.4. Install python libraries (for the client side):

```sh
$ sudo apt-get install python-requests
```

## 3. JSON server.

Create .json such that (tasks.json):

```json
{
    "tasks": [
        {
          "id": 1,
          "summary": "Shower",
          "description": "Take a f***cking shower"
        }
    ]
}
```

## 4. Python client scripts.

 - GET command example:

```sh
$ python GET_client_example.py
Task ID: 1
Task summary: Shower
Full description: Take a fucking shower
```

 - POST command example:

```sh
$ python POST_client_example.py
New task added with ID: 2
Task summary: Coffee
```
It should be seen the new task added to http://localhost:3000/tasks

## 5. API

First prototype: `mes_api.py` with basic REST commands.
Test 1.0:

```sh
$ python api_tasks_test.py
REST API TEST 1.0


Enter task name: Dog
Enter task description: Take the dog out for a walk
New task added with ID: 3
Task summary: Dog


     >> Current task list:


Task ID: 1
Task summary: Shower
Full description: Take a fucking shower


Task ID: 2
Task summary: Coffee
Full description: Make some coffee


Task ID: 3
Task summary: Dog
Full description: Take the dog out for a walk
```
