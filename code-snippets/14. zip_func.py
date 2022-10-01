# - Zip Function Tutorial - #

fields = ['First Name', 'Last Name', 'Gender', 'Age']
values = ['John', 'Doe', 'Male', 25]

# Print the values from each list in parallel
for field, value in zip(fields, values):
    print(f"{field}: {value}")
