# Writing to a file

with open("output.txt", "w") as file:
	file.write("This is the first line of text in this file\n")
	file.write("This is the second line of text in this file\n")

# Appending content to the file
with open("output.txt", "a") as file:
	file.write("This content is appended to the file\n")
