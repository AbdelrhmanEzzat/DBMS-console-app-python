from colorama import Fore

print(Fore.RED + '__________ Welcome to Registration Form __________')



def log_reg():
    while True:
        print("1. Login ")
        print("2. Registration ")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            from User.Login__ import login_user
            login_user()

        elif choice == "2":
            from User.Registration__ import info
            myinfo = info()

            from FileOperations.fileHandler__ import read_data
            read_data()

            from FileOperations.fileHandler__ import write_data

            write_data(myinfo)
            while True:
                print("1. Login ")
                print("0. Exit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    from User.Login__ import login_user
                    login_user()
                elif choice == "0":
                    break



        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
log_reg()






#
# login_user()
#
# user_id = login_user()
#
# main_menu()






