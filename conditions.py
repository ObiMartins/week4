# Demonstrating how Python scripts make decisions
environment = "production"
if environment == "production":
	print("Out of bound! this is production environment")
else:
	print("Non-production environment")

# Testing if a variable is empty
print()
print("===========================")
app_name = ""
if app_name == "":
	print("App name cannot be empty")
else:
	print(f"App name is {app_name}")

# Loop
print()
print("=========Loop==========")
files = ["app.log", "error.log", "access.log"]
for file_names in files:
	print(f"Processing {file_names}")
