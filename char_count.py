# Character count
def char_count():
    try:
        name = input("enter your string: ")
        if name.isalpha() == True or name.isspace() == False:
            count_char = len(name)
            print("The number of Characters are :",count_char)
        else:
            print("Enter character type..!")
    except ValueError:
        print("Check the Value you entered")
        char_count()

char_count()