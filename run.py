#!/usr/bin/python3

import sys, os, json, requests

server_location = "http://" + sys.argv[1] + "/feedback/"
file_list = os.listdir("/data/requests")
current_request = {}

for file in file_list:
    #set up the dictionary for the request
    open_file = open(file,r)
    line_list = open_file.read().splitlines()
    current_request["title"] = line_list[0]
    current_request["date"] = line_list[1]
    current_request["name"] = line_list[2]
    current_request["feedback"] = line_list[3]
    open_file.close()

    post = requests.post(server_location,json=current_request)
    post.raise_for_status()