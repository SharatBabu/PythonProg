def contact_list():
    try:
        name = []
        number = []
        while True:
            option = int(input("1. Add Contact\n2. Search contact\n3. Remove contact\n4. Show contact\n5. Quit\nEnter your option:"))
            if 0 < option < 5:
                if option == 1:
                    x = input("Enter the name : ")
                    name.append(x);
                    y = int(input("Enter the number : "))
                    number.append(y)

                elif option == 2:
                    x = input("Enter the name to Search : ")
                    if x in name:
                        index = name.index(x)
                        print("Name : ",name[index])
                        print("Number : ",number[index])
                        print("Contact added successfully")

                    else:
                        print("No Name in contact list")

                elif option == 3:
                    x = input("Enter the name to Search : ")
                    if x in name:
                        ind = name.index(x)
                        name.remove(ind)
                        number.remove(ind)
                        print("Contact removed successfully.")

                    else:
                        print("No Name in contact list")

                elif option == 4:
                    for i in range(len(name)):
                        print(name[i],"------",number[i])
                else:
                    print("Thank you..")
                    quit()
            else:
                print("Choose on in option.")

    except ValueError:
        print("Enter appropriate values..")
        contact_list()

contact_list()