#program to Convert any string into Upper,Lower,Camel cases
def convert_case():
    try:
        name = input("enter your string: ")
        if (name.isalpha()) == True:
            upc = name.upper()
            lc = name.lower()
            cc = name.title()
            print("String in Upper case ",upc)
            print("String in Lower case ",lc)
            print("String in Camel case ",cc)
        else:
            print("Enter String value")
            convert_case()
    except ValueError:
        print("Enter valid input..")

convert_case()