# Reading JSON from a file

import json

with open("config.json", "r") as file:
	data = json.load(file)
	print(data["app_name"])
	print(data["port"])
	print(data["environment"])
