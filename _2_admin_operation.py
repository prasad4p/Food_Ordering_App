from _1_admin import Admin

class Operation:
    food_list = []

    def add_food_items(self):
        FoodId = int(input("Enter the ID of Food Item : "))
        Name = input("Enter the Name of Food Item : ")
        Quantity = int(input("Enter the Quantity of Food Item : "))
        Price = float(input("Enter the Price of Food Item : "))
        Discount = int(input("Enter the Dicount on Food Item : "))
        Stock = int(input("Enter the Stock of Food Remain : "))
        admin_obj = Admin(FoodID=FoodId,Name=Name,Quantity=Quantity,Price=Price,Discount=Discount,Stock=Stock)
        self.food_list.append(admin_obj)
        print("Food Item Added Successfully !")

    def Edit_food_items(self):
        FoodID = int(input("Enter the FoodID to Edit Food Item : "))
        for foods in self.food_list:
            if foods.get_id() == FoodID:
                Name = input("Enter the Name of Food Item : ")
                Quantity = int(input("Enter the Quantity of Food Item : "))
                Price = float(input("Enter the Price of Food Item : "))
                Discount = int(input("Enter the Dicount on Food Item : "))
                Stock = int(input("Enter the Stock of Food Remain : "))
                foods.set_Name = (Name)
                foods.set_Quantity = (Quantity)
                foods.set_Price = (Price)
                foods.set_Discount = (Discount)
                foods.set_Stock = (Stock)
            
        else:
                print("Food Item Not Found")

    def view_food_items(self):
        for i in self.food_list:
           print(i,"\n") 
           break
        else:
            print("Food Item Not Found")

    def remove_food_items(self):
        FoodID = int(input("Enter the FoodID to Remove Food Item : "))
        for foods in self.food_list:
            if foods.get_id() == FoodID:
                self.food_list.remove(foods)
                print("Food Item Successfully Remove!")
                break
        else:
            print("Food Item Not Found")