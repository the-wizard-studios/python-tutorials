import os


# Variables
current_directory = os.path.dirname(os.path.realpath(__file__))
# print(current_directory)

# Write to file
def write_to_file(file_path, file_contents):
    print("- Write to File -")
    with open(file_path, 'w+') as f:
        # Automatically creates the file if it does not exist and writes the content to it
        f.write(file_contents)

# Read file
def read_from_file(file_path):
    print("- Read From File -")

    with open(file_path, 'r') as f:
        file_contents = f.read()
    
    return file_contents

# main
if __name__ == "__main__":
    # Define File
    file_name = "File Handling (Part 1).txt"
    file_path = os.path.join(current_directory, file_name)

    # Write to File
    # write_to_file(file_path, "Hello World")

    # Now, let's read from the file
    # Read from file
    file_contents = read_from_file(file_path)
    print(file_contents)