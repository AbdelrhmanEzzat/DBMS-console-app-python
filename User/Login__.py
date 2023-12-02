import json
from User.Project__ import *
from colorama import Fore

def main_menu(user_id):
    while True:
        print(Fore.CYAN +"1. Create a project")
        print(Fore.CYAN +"2. View all projects")
        print(Fore.CYAN +"3. View User projects")
        print(Fore.CYAN +"4. Edit a project")
        print(Fore.CYAN +"5. Delete a project")
        print(Fore.CYAN +"6. Search projects by date")
        print(Fore.CYAN +"0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_project(user_id)
        elif choice == "2":
            view_all_projects()
        elif choice == "3":
            view_projects(user_id)
        elif choice == "4":
            edit_project(user_id)
        elif choice == "5":
            delete_project(user_id)
        # elif choice == "6":
        # #     search_projects_by_date()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")






def login_user():

    #global flag_login  # Declare flag_login as a global variable
    while True:
        print("1. Login ")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
        # Prompt the user for login credentials
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            with open('Users.json', 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    for user in data:
                        if user['Email'] == email and user['Password'] == password:
                            print(Fore.BLUE +"Login successful!")
                            print(Fore.YELLOW +"==========================")
                            user_id = user['id']
                            #flag_login = True
                            #return user_id
                            #user_id = login_user()
                            # If the login is successful, go to the main menu
                            #if flag_login:
                            main_menu(user_id)

                    print("Invalid email or password. Please try again.")
        elif choice == "0":
            break
# Call the login_user function to start the login process




# user_id = login_user()
#         # If the login is successful, go to the main menu
# if flag_login:
#     main_menu()

