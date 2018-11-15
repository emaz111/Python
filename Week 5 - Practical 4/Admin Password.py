"""

Password Checker

This program allows the admin to prevent users from entering specified names and their username as their new password

The program asks the user to enter their username and password which are stored in two variables. After logging in the
user is asked to change their old password to the new one. If the user enters their username or the specified words
as their new password then it will output an error and continue to loop until a suitable password has been entered

"""
"""
__Author__ = Emaz Khan
__Email__ = U1859269@unimail.hud.ac.uk
__Date__ = Thursday 1st November 2018
"""

Username = input("Enter the username: ")
Password = input("Enter the password: ")
New_Password = " "

while True:
    New_Password = input("Enter your new password: ").lower()
    if New_Password == Username or New_Password == "huddersfield" or New_Password == "justinbieber" \
    or New_Password == "cheese" or New_Password == "canalside":
        print("Invalid Password")
    else:
        print("Password changed successfully!")
        break
