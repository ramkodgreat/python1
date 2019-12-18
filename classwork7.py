"""
    User registration, Login and authentication
    program
"""
def welcome(message="Welcome please register here",symbol="*"):
    view = 30 * symbol
    print(view)
    print(message)
    print(view)


welcome()



"""
    Collection and validation of user inputs
"""


username = input("Enter your username")

while len(username) >= 10:
    print("Username must not exceed 10 characters *Please enter your user name again")

email = input("Enter your email *Email must contain @ symbol")

firstname = input("Enter your firstname here")

lastname  = input("Enter your lastname here")

password = input("Enter your password here")

confirm_password = input("Confirm your password")

while password != confirm_password:
    print("Passwords do not match please try again")
    password = input("Enter your password here")
    confirm_password = input("Confirm your password")

"""
    Creating a dictionary of user data
"""
user = {}
user["username"] = username
user["email"] = email
user["firstname"] = firstname
user["lastname"] = lastname
user["password"] = password

"""
    Saving user data in a list
"""
user_save = []
user_save.append(user)
print(user_save)


"""
    Registration  complete view function
"""
def complete():
    view = 80 * "*"
    print(view)
    for user in user_save:
        print("Congratulations",user["username"],"your registration is complete Proceed to log in")
    print(view)


complete()


"""
    User Authentication and Login
"""

"""
    login welcome view function
"""
def login_welcome():
    view = 70 * "*"
    print(view)
    print("You are currently logged in")
    print(view)


email = input("Enter your email to login")
password = input("Enter your password here")
for user in user_save:
    while user["email"] != email and user["password"] != password:
        print("Invalid username or password") 
        email = input("Enter your email to login")
        password = input("Enter your password here")

login_welcome()