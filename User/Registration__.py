import re
from colorama import Fore
import json
def info():
    id = 1

    with open('Users.json', 'r') as file:
        data = json.load(file)
        if isinstance(data, list):
            for user in data:
                if user['id'] == id:
                    id += 1


        # Check if the ID already exists in the users dictionary


    while True:
        # Name Validation
        first_name = input("Enter your First Name: ")
        first_name_v = first_name.strip().lower()
        if first_name_v.isalpha():
            print(Fore.MAGENTA + "your name in in correctly way")
            break

        else:
            print(Fore.RED + "your name is not valid ! " , first_name)



    while True:
        last_name = input("Enter your Last Name : ")
        last_name_v = last_name.strip().lower()
        if last_name_v.isalpha():
            print(Fore.MAGENTA + "your name IS in correctly way")
            break
        else:
            print(Fore.RED + "your name is not valid ! ", first_name)


# Name Validation
    while True:
        email = input("Enter your Email: ")
        email_v = email.strip().lower()
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email_v):
            print(Fore.RED + "your name is not valid ! ", email)


        else:
            print(Fore.MAGENTA + "your email is correct ^_^")
            break

#  Validate password and confirm password (should match and have at least 8 characters)
    while True:
        password = input("Enter your password : ")
        confirm_password = input("Enter your Confirm password : ")
        if password != confirm_password or len(password) < 8:
            print(Fore.RED + "your Password IS dosn't match or grater than 8 ")

        else:
            print(Fore.MAGENTA + "your Password  is  valid ")
            break



# Validate mobile phone number (should be a valid Egyptian phone number)
    while True:
        phone = input("Enter your Phone number : ")
        phone_pattern = r'^01[0-2]\d{8}$'
        if not re.match(phone_pattern, phone):
            print(Fore.RED + "your phone Is invalid ! ")


        else:
            print(Fore.MAGENTA + "your phone  is  valid ")
            break

    myinfo = {"First Name": first_name_v,
          "Last Name": last_name_v,
          "Email": email_v,
          "Password": password,
          "Phone": phone,
        "id": id}
    id += 1

    print(Fore.YELLOW +"Your Inputs Data are : ")
    print(myinfo)

    return myinfo

#
# from User.Login__ import login_user
# def log():
#     while True:
#         print("1. Login ")
#         print("0. Exit")
#
#         choice = input("Enter your choice: ")
#
#         if choice == "1":
#             login_user()
#
#         elif choice == "0":
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
# log()
#
