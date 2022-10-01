import os
import pandas as pd


# Current Script Name
CURRENT_SCRIPT_NAME = os.path.basename(__file__).split('.')[0]

# Directories
CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


# Read Excel
def read_excel(excel_file):

    df = pd.read_excel(excel_file)

    # Convert to List
    df_list = df.values.tolist()

    # Create a list of dictionaries to store the values
    students = []

    for data in df_list:
        student = {}

        student['first_name'] = data[0]
        student['last_name'] = data[1]
        student['age'] = data[2]

        # Append to list
        students.append(student.copy())
    
    return students


# Main
if __name__ == "__main__":

    # Excel File
    excel_file = os.path.join(CURRENT_DIRECTORY, 'students.xlsx')

    # Read Excel
    students = read_excel(excel_file)

    # You can manipulate the data as per your needs now that it's in a list of dictionaries

    # Example, print the data
    for student in students:
        print(student)
