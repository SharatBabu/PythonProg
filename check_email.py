#Program to check the given email is valid or not
def check_email():
    try:
        import re   # importing regular expressions
        email = input("Please type in an email address :")
        if re.match("\A(?P<name>[\w\.\_\1-9\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
            print("EmailId is valid")
        else:
            print("EmailId is invalid")
            check_email()
    except ValueError:
        print("Enter Valid EmailId..!")
        check_email()

check_email()
