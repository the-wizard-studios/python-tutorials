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

# - Call the functions -
# Hello World
hello_world()

# Say Hi
say_hi("John")

# Calculate Sum
sum = calaculate_sum(5, 10)
print("Sum is {sum}".format(sum=sum))
