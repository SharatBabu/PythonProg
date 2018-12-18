#program to print previous prime
def prev_prime():
    try:
        number = int(input("Enter the num: ")) - 1
        while(True):
            res=prevPrime(number)
            if res:
                print("The previous prime number is: ",number)
                break
            number -= 1
    except ValueError:
        print("Enter numeric values.")
        print("----------------------------------------")
        prev_prime()

def prevPrime(number):
    for i in range(2,number):
        if number%i == 0:
            return False
        sqr=i*i
        if sqr>number:
           break
    return True
prev_prime()