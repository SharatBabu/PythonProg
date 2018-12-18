def currency_count():
    try:
        notes = [2000,500,200,100,50,20,10,5,2,1]
        value = int(input("Enter the amount :"))
        j = 0
        for i in range(0,10):
            if value >= 0:
                if value >= notes[i]:
                    j += 1
                    value = value - notes[i]
        print("Minimum notes/coin required are:", j)
    except ValueError:
        print("Enter a valid amount..")
        currency_count()

currency_count()
