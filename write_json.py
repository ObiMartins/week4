# Writing JSON to a file

import json

print("================dump=========")

config = {
"app_name": "inventory-service",
"port": 8080,
"environment": "production"
}

with open("output.json", "w") as file:
	json.dump(config, file, indent=2)


print()
print("=============dumps==================")

json_text = json.dumps(config, indent=2)
print(f"{json_text}")
