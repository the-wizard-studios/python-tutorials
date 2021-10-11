'''
# Without try..except
## Try to divide by 0
x = 2/0
print(x)

# Script Fails!
'''

'''
# Handle the error
try:
    x = 2/0
except ZeroDivisionError:
    print("You cannot divide by 0")
'''

# A more general approach
try:
    x = 2/0
except Exception as e:
    # Handles any error which occurs
    print("Error: {e}".format(e=e))

    # Print the traceback
    import traceback
    print(traceback.format_exc())

# Script did not fail => We handled the error and displayed what and where there is something wrong with the script.

# Note: However, wherever possible, you should always catch and handle the specific error instead of catching all errors.
