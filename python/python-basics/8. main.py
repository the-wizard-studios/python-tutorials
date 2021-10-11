# Functions
'''
# Syntax
def <function name>(paramters):
    <define function logic>
'''

# 'Hello World' Function => No Input Parameters
def hello_world():
    # Simply prints 'Hello World'
    print("Hello world")

# More Examples
# 'Say Hi' Function => 1 Input Parameter
def say_hi(name):
    # Says Hi to the name given as parameter
    print("Hi {name}".format(name=name))

# 'Calculate Sum' Function => 2 Input Parameters, Returns Output
def calaculate_sum(num_1, num_2):
    # Calculate the sum of 2 numbers given as parameters
    sum = num_1 + num_2

    # Return the result
    return sum

# Execute the script
#  ==> Nothing Happens - You need to explicitlty call the functions to be able to use them!

# Define a main function to use the above functions

# This is the 'function' that will be called when you execute your script
if __name__ == "__main__":
    # Hello World
    hello_world()

    # Say Hi
    say_hi("John")

    # Calculate Sum
    sum = calaculate_sum(5, 10)
    print("Sum is {sum}".format(sum=sum))

# Now, let's run the script again
# Now the functions are executed!