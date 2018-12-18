# Program to greet the user according to the time
def greet_ac_time():

    name = input("enter your name: ")
    if(name.isalpha())== True:
        import datetime
        now = datetime.datetime.now()
        time = str(now.time())
        if (int(time[:2]) < 12):
            print('Good Morning', name)
        elif (12 <= int(time[:2]) <= 17):
            print('Good Afternoon', name)
        elif (17 <= int(time[:2]) <= 20):
            print('Good Evening', name)
        else:
            print('Good Night', name)
    else:
        print("You have not entered proper name..!")
        greet_ac_time()

greet_ac_time()