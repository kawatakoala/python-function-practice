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
triangle = [[1], [1, 1]]


def pascal(n):
    # base case
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        # fill up correct number of rows in triangle
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            # create correct row, then add to triangle (this row will be 1 longer than row before it)
            length = len(row_prev)+1
            for i in range(length):
                # first number is 1
                if i == 0:
                    row.append(1)
                # intermediate nunmbers get added from previous rows
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1]
                               [i-1]+triangle[row_number-1][i])
                # last number is 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        # print triangle
        for row in triangle:
            print(row)


pascal(3)
pascal(5)
