#!/usr/bin/python

######################
### MES SYSTEM API ###
######################

# For now, just a prototype

import requests

# Requires definition of URL in the main
# _url = http://localhost:3000/ for example  

#### BASIC SET ####

# Function to get orders
def get_orders(_url, path):
    g_url = _url + path
    return requests.get(g_url)

# Function to add a new order
def new_order(_url, path, summ, descr):
    p_url = _url + path
    ordered = {"summary": summ, "description": descr }
    return requests.post(p_url, json=ordered)

# Function to delete completed orders
def completed_order(_url, path, order_id):
    d_url = _url + path + '{:d}/'.format(order_id)
    return requests.delete(d_url)


# Function to update an order
def update_order(_url, path, order_id, summ, descr):
    u_url = _url + path + '{:d}/'.format(order_id)
    updates = {"summary": summ, "description": descr }
    return requests.post(p_url, json=ordered)

#####################