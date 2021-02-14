# james jack
# 2/13/2021

# program that specifies if numbers are divisible by 3 or 5 with a print statement from 1-50

for i in range(1, 51, 1):  # specifies the range of numb 1-50 to be listed in 1-50
    if i % 3 == 0:         # if the number has zero remainder, it is divisible by 3
        print("divisible by three")  # prints statement
    elif i % 5 == 0:        # else if the number has zero remainder, it is divisible by 5
        print("divisible by 5")     # prints statement
    elif i % 3 == 0 and i % 5 == 0:     # else if it has no remainder from 3 or 5 it is divisible by both
        print("divisible by both")      # print statement
    else:
        print(i)                    # if not divisible, just print the number
