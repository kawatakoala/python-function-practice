# 1 Write a Python function called max_num()to find the maximum of three numbers.
def max_num(x, y, z):
    return max([x, y, z])


print(max_num(5, 3, 2))


# 2 Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


list1 = [3, 2, 4]
print(mult_list(list1))


# 3 Write a Python function called rev_string() to reverse a string.
def rev_string(x):
    return x[::-1]


mytxt = rev_string("Michael Kawata")
print(mytxt)


# 4 Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(x, y, z):
    return x in range(y, z+1)


print(num_within(1, 2, 3))
print(num_within(200, 100, 1000))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
