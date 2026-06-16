# Demonstrating dictionary variable
config = {
"app_name": "inventory-service",
"port": 8080,
"environment": "staging"
}
print(config["app_name"])
print(config["port"])
print(config["environment"])

# Dictionaries are useful when dealing with configurations and structured data
print("=======================")
server = {
"name": "web-1",
"ip": "192.168.1.10",
"role": "frontend"
}
print(f"{server["name"]} -> {server["ip"]}")
