#!/usr/bin/env python3

import os
import requests

ip_address = ""
server_location = "http://" + ip_address + "/feedback/"
file_list = os.listdir("/data/feedback")
current_request = {}

for file in file_list:
    #set up the dictionary for the request
    open_file = open("/data/feedback/"+file,"r")
    line_list = open_file.read().splitlines()
    current_request["title"] = line_list[0]
    current_request["name"] = line_list[1]
    current_request["date"] = line_list[2]
    current_request["feedback"] = line_list[3]
    open_file.close()

    new_post = requests.post(server_location,json=current_request)
    new_post.raise_for_status()
    print(new_post.status_code)