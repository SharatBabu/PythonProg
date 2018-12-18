# program to sum all odd and even in the list
def sum_odd_even():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_num = 0
    even_num = 0
    for i in list1:
        if i % 2 != 0:
            odd_num += i
        else:
            even_num += i
    print("Sum of Odd is ", odd_num,"\nSum of Even is", even_num)

sum_odd_even()