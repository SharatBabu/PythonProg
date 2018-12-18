def prime_or_not():
    try:
       num = int(input("Enter number to check:"))
       if 2 <= num:
           n = num//2
           for i in range(2, n):
                if n % i == 0:
                    flag = 1
                    break
                else:
                    flag = 0
           if flag == 1:
                print(num, "is not Prime")
           else:
                print(num, "is Prime")
    except ValueError:
        print("Enter numeric values.")
        prime_or_not()

prime_or_not()