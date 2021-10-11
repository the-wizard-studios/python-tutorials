'''
Ask the user for an input
For example, ask user for his/her name and output the name
'''

# Ask for name and store it in a 'name' variable
name = input("Enter your name: ")

# Output the name
# print(name)

# Say Hi
# print("Hi " + name)

# A better way => Use format string
# print("Hi {name}".format(name=name))

# Using f-strings (Note: f-strings will work only with Python 3.6 and above)
print(f"Hi {name}")