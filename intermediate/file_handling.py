# Python File Handling

# Write to a file

file = open("test.txt", "w")

file.write("Hello Python")

file.close()


# Read a file

file = open("test.txt", "r")

content = file.read()

print(content)

file.close()


# Add new text to a file

file = open("test.txt", "a")

file.write("\nHello again")

file.close()
