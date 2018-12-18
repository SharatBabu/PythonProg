# program to find greatest number in list
def greater_num():
    list1 = [1, 2, 3, 4, 5, 98, 6, 9, 10, 23, 54, 56, 29, 76]
    num = 0
    for i in list1:
        if num < i:
            num = i
    print("The largest in the list is ", num)

greater_num()