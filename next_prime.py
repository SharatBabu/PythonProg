#Program to fine next prime
def next_prime():
    try:
        number = int(input("Enter the num: ")) + 1
        while(True):
            res=nextPrime(number)
            if res:
                print("The next prime number is: ",number)
                break
            number += 1
    except ValueError:
        print("Enter numeric values.")
        print("----------------------------------------")
        next_prime()

def nextPrime(number):
    for i in range(2,number):
        if number%i == 0:
            return False
        sqr=i*i
        if sqr>number:
           break
    return True
next_prime()