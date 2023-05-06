def max_num(x, y, z):
    return max([x, y, z])


print(max_num(5, 3, 2))


def mult_list(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


list1 = [3, 2, 4]
print(mult_list(list1))
