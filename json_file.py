# Parsing JSON string to Python object
import json

data = '{"environment": "Production", "port": 8080}'
parsed = json.loads(data)
print(parsed["environment"])
print(parsed["port"])
