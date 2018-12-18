# program to print factorial of given number
def fact_num():
    try:
        num = int(input("Enter the number to find factorial: "))
        n = 1
        for i in range(1, num+1):
            n = n * i
        print("The factorial is : ", n)
    except ValueError:
        print("Enter a valid input..")
        print("----------------------------------------")
        fact_num()

fact_num()