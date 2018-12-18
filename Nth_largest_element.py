# Program to find nth largest element from typing import List
import _pytest
def nth_element():
    try:
        list1 = []
        new_list = []
        num = int(input("Ënter the length of the list : "))
        for i in range(1, num+1):
            x = int(input("Enter the value to list: "))
            list1.append(x)
        #list1.sort()
        while list1:
            minimum = list1[0]  # arbitrary number in list
            for x in list1:
                if x < minimum:
                    minimum = x
            new_list.append(minimum)
            list1.remove(minimum)
        n = int(input("Enter the nth value to search: "))
        print('The Nht largest number : ', new_list[num - n])
    except ValueError:
        print("Enter Valid input..")
        print("----------------------------------------")
        nth_element()


nth_element()
