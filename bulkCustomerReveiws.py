#! /usr/bin/env python3
__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/4/2020"

import os
import requests

list_of_files = os.listdir("/data/feedback/")
url = "http://<corpweb-external-IP>/feedback"
dict = {}
for file in list_of_files:
    if file.startswith("."):
        continue
    with open(os.path.join("/data/feedback",file),"r") as current_file:
        title = current_file.readline().strip()
        name = current_file.readline().strip()
        date = current_file.readline().strip()
        feedback = current_file.readline().strip()
        dict = {"title":title, "name":name, "date":date, "feedback":feedback}

    response = requests.post(url, json=dict)
    if not response.ok:
        print(response.status_code)
    elif response.status_code == 201:
        print("Status posted Successfully")
