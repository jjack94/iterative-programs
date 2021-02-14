# James Jack
# 2/13/21
# 1st part- program prints each numb on list to new line
# 2nd part- prints each numb and their respective square to new line
# 12, 10, 32, 3, 66, 17, 42, 99, 20 is list
# list of numbers
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for i in numbers:  # for loop to print numbers individually and not as list
    print(i)

for i in numbers:  # for loop with "squared" is that takes each number and puts it to the power of 2 (squares them)
    print(i, "squared is", i ** 2)
