import os
import json
import logging
import datetime
import subprocess


# - Global Variables -

# Current Script Name
CURRENT_SCRIPT_NAME = os.path.basename(__file__).split('.')[0]

# Directories
CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
LOGS_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "Logs")

# Current Year-Month
CURRENT_YEAR_MONTH = datetime.datetime.now().strftime("%Y-%m")


# Logger
def logger():

    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(funcName)s : %(lineno)d : %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

    # Logger file name
    log_file_name = f"{CURRENT_YEAR_MONTH}_{CURRENT_SCRIPT_NAME}.log"

    # Check if LOG folder exists
    if not os.path.exists(LOGS_DIRECTORY):
        # Create Folder 'logs' since it does not exists
        os.makedirs(LOGS_DIRECTORY)

    # Log file path
    log_file = os.path.join(LOGS_DIRECTORY, log_file_name)

    # File Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    LOG.addHandler(file_handler)
    
    # StreamHandler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    LOG.addHandler(stream_handler)

    return LOG


# Execute Command
def execute_command(shell_command):
    LOG.debug("- Execute Command -")

    LOG.debug("Shell Command: {shell_command}".format(shell_command=shell_command))

    output_msg = ""

    try:
        result = subprocess.Popen(['powershell', shell_command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        output, error = result.communicate()

        output = output.decode(encoding="utf-8", errors="ignore")
        error = error.decode(encoding="utf-8", errors="ignore")

        output_msg += str(output)

        # LOG.debug("Output: {output}".format(output=output))
        # LOG.debug("Error: {error}".format(error=error))

        return output

    except Exception as e:
        LOG.error("Failed to execute command")
        LOG.error(e, exc_info=True)


# Main
if __name__ == "__main__":
    
    # LOG
    LOG = logger()

    LOG.debug("--- Start ---")

    try:
        # Shell Command
        shell_command = "pwd | ConvertTo-Json"

        # Execute Command
        output_msg = execute_command(shell_command)

        # Convert to dict
        output_msg = json.loads(output_msg)
        
        # print(output_msg)

        # Write to File
        with open(os.path.join(CURRENT_DIRECTORY, f'{CURRENT_SCRIPT_NAME}.json'), mode='w+', encoding='utf-8') as f:
            f.write(json.dumps(output_msg, indent=4))

        """
        Now, you can retrieve any value you want.

        For example, to retrive the 'CurrentLocation', do the following: 
        """

        # Extract Current Location
        current_location = output_msg['Drive']['CurrentLocation']

        print(f"\nCurrent Location: {current_location}\n")

    except Exception as e:
        LOG.error("Failed")
        LOG.error(e, exc_info=True)
    finally:
        LOG.debug("--- End ---")
