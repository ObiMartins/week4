# Open, Read and Close the file

file = open("note.txt", "r")
content = file.read()
print(content)
file.close()

# Prefered pattern. This closes the file automatically

print("=======This file closed automatically by using with open===========")
with open("note.txt", "r") as file:
	content = file.read()
	print(content)

# This read the file line by line
print()
print("===========Reading the file line by line==========")
with open("note.txt", "r") as file:
	for line in file:
		print(line.strip())
