

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    def place_new_order(self):
        print("Welcome to the restaurant! Here's our menu:\n")
        menu = {
            1: "Tandoori Chicken (4 pieces) [INR 240]",
            2: "Vegan Burger (1 Piece) [INR 320]",
            3: "Truffle Cake (500gm) [INR 900]"
        }
        for item_number, item_description in menu.items():
            print(f"{item_number}. {item_description}")
        order_numbers = input("Please enter the numbers of the items you want to order, separated by commas: ")
        order_numbers = [int(n) for n in order_numbers.split(",")]
        order_items = [menu[n] for n in order_numbers]
        print("You have ordered the following items:\n")
        for item in order_items:
            print(item)
        confirm_order = input("Do you want to confirm your order? (yes/no): ")
        if confirm_order.lower() == "yes":
            self.order_history.append(order_items)
            print("Order confirmed!")
        else:
            print("Order cancelled.")

    def show_order_history(self):
        if not self.order_history:
            print("No orders found in history.")
        else:
            print("Order history:")
            for i, order in enumerate(self.order_history, start=1):
                print(f"{i}. {order}")

    def update_profile(self):
        print("Update your profile:\n")
        self.full_name = input("Full Name: ")
        self.phone_number = input("Phone Number: ")
        self.email = input("Email: ")
        self.address = input("Address: ")
        self.password = input("Password: ")


    def register(self):
        print("Register on the application:\n")
        full_name = input("Full Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")
        password = input("Password: ")
        user = User(full_name, phone_number, email, address, password)
        print("Registration successful!")
        return user


    def login(users):
        print("Log in to the application:\n")
        email = input("Email: ")
        password = input("Password: ")
        for user in users:
            if user.email == email and user.password == password:
             print("Login successful!")
            return user
        print("Invalid email or password.")
        return None
    


