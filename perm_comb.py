# Program to find permutation and combinations
def perm_comb():
    try:
        select = int(input("Select your option\n1. Permutation\n2. Combination\nSelection : "))
        if( 1 <= select <= 2):
            n = int(input("Enter the n value : "))
            r = int(input("Enter the r value : "))
            if select == 1:
                res = per_fun(n,r)
                print(res)
            else :
                res1 = comb_fun(n,r)
                print(res1)
        else:
            print("Select one from options..")
            print("----------------------------------------")
            perm_comb()
    except ValueError:
        print("Only Integer values are allowed..")
        print("----------------------------------------")
        perm_comb()

def per_fun(a,b):
    n = 1
    for i in range(1, a + 1):
        n = n * i
    m = 1
    d = a-b
    for j in range(1, d + 1):
        m = m * j
    pnr = n * m
    return(pnr)

def comb_fun(a,b):
    n = 1
    for i in range(1, a + 1):
        n = n * i
    m = 1
    for j in range(1, b + 1):
        m = m * j
    c = a- b
    p = 1
    for k in range(1, c + 1):
        p = p * k
    ncr = n/(m*p)
    return(ncr)

perm_comb()