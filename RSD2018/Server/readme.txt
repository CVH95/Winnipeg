The MES system is made in Python3 and are using Flask with a SQL extension for the REST api.

The system also need a MySQL v8 db to run. 

Included are a python file for the Flask server and a SQL export, that shows the structure of the "rsd" SQL db.

In the Python code you can see the configuration for the database in order for the python code to access the SQL db.

Note: the MES server will automatic add more jobs, when they are below 5. This is just a sample code - the final system have another behavior, but this shows the idea.

