# Variables
num_1 = 15
num_2 = 10

# If Condition
## Check if num_1 is smaller than num_2
if num_1 < num_2:
    print("num_1: {num_1} is smaller than num_2: {num_2}".format(num_1=num_1, num_2=num_2))
elif num_1 == 15:
    print("num_1: {num_1} is equal to 15".format(num_1=num_1))
    # Did not go to else!
else:
    print("num_1: {num_1} is greater than num_2: {num_2}".format(num_1=num_1, num_2=num_2))