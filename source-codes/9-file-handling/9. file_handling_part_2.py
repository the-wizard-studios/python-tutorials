import os


# Variables
current_directory = os.path.dirname(os.path.realpath(__file__))

# Write to file
def write_to_file(file_path):
    print("- Write to File -")
    
    with open(file_path, 'w+') as f:
        # Write Numbers 1 to 10 to file
        for number in range(1, 11):
            '''
            # Convert number to string before writing to file
            ==> Syntax: str(<what you want to convert to string>)
            '''
            f.write("{number}\n".format(number=str(number)))


# Read file
def read_from_file(file_path):
    print("- Read From File -")

    with open(file_path, 'r') as f:
        file_contents = f.readlines()

    return file_contents

# main
if __name__ == "__main__":
    
    # Define File
    file_name = "File Handling (Part 2).txt"
    file_path = os.path.join(current_directory, file_name)

    # Write to File
    # write_to_file(file_path)

    # Read from file
    file_contents = read_from_file(file_path)
    for file_content in file_contents:
        print(file_content.strip())