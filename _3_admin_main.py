from _2_admin_operation import Operation 

class Main():
    def execute(self,choice,operation):
        if choice == 1:
            print("******Add Food Item*******")
            operation.add_food_items()
        if choice == 2:
            print("********Edit Food Item******")
            operation.Edit_food_items()
        if choice == 3:
            print("******View Food Items******")
            operation.view_food_items()
        if choice == 4:
            print("********Remove Food Item******")
            operation.remove_food_items()

if __name__ == "__main__":
    
    operation = Operation()
    main = Main()
    while True:
        choice = int(input("Enter \n1.Add Food Item \n2.Edit Food Item \n3.View Food Items \n4.Remove Food Item By FoodID : \n"))
        main.execute(choice=choice,operation=operation)           