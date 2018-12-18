# program on tea stall
def tea_stall():
    try:
        option = int(input("Menu\n1.Tea\n2.Coffee\n3.Milk\n Place order : "))
        tea = 0
        coffee = 0
        milk = 0
        if 0 < option < 4:
            if option == 1:
                tea = tea+1
                print("You have ordered Tea")
            elif option == 2:
                coffee = coffee+1
                print("You have ordered Coffee")
            elif option == 3:
                milk = milk+1
                print("You have ordered Milk")
            else:
                print("You have to choose one of the option")
            print("Over all order til now are \nTea =", tea, "\nCoffee = ", coffee, "\nMilk = ", milk)
        else:
            print("You have to select in the menu only..")
    except ValueError:
        print("Enter one of the options")

tea_stall()
