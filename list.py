
# Create a list and print list items at different index 
environment = ["dev", "staging", "production"]
print(environment)
print(environment[0])
print(environment[1])
print(environment[2])

# Looping through the list
print()
print("Looping through the list")
for evn in environment:
	print(evn)

# Checking servers
print()
servers = ["web-1", "web-2", "web-3"]
for server in servers:
	print(f"Checking {server}")
