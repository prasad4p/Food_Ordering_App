from _4_user import User 

class Main():
    def execute(self,choice,operation):
        if choice == 1:
            print("******Register*******")
            operation.register()
        if choice == 2:
            print("*******Log in*******")
            operation.login()
        if choice == 3:
            print("******Place New Order******")
            operation.place_new_order()
        if choice == 4:
            print("********Order History******")
            operation.show_order_history()
        if choice == 5:
            print("*******Update Profile*******")
            operation.update_profile()
        if choice == 6:
            print("********Thnak You! Visit Again******")
            


if __name__ == "__main__":
    full_name = input("Enter the Name :")
    phone_number = int(input("Enter the phone Number :"))
    email = input("Enter the email :")
    address = input("Enter the Address :")
    password = input("Enter the Password :")

    operation = User(full_name, phone_number, email, address, password)
    main = Main()
    while True:
        choice = int(input("Enter \n1.Register \n2.Log in \n3.Place New Order \n4.Order History \n5.Update Profile \n6.Quit : \n"))
        main.execute(choice=choice,operation=operation) 