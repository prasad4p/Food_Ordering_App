class Admin:

    def __init__(self,FoodID,Name,Quantity,Price,Discount,Stock):
        self.FoodID = FoodID
        self.Name = Name
        self.Quantity = Quantity
        self.Price = Price
        self.Discount = Discount
        self.Stock = Stock

    def __str__(self):
        return f"FoodID :{self.FoodID}\nFood Name :{self.Name}\nFood Quantity :{self.Quantity}\nPrice of Food :{self.Price}\nDicount of Food :{self.Discount}\nStock Remain :{self.Stock}"
    
    def get_id(self):
        return self.FoodID
    def set_id(self,FoodID):
        self.FoodID = FoodID

    def get_name(self):
        return self.Name
    def set_name(self,Name):
        self.Name = Name

    def get_quantity(self):
        return self.Quantity
    def set_quantity(self,Quantity):
        self.Quantity = Quantity

    def get_price(self):
        return self.Price
    def set_price(self,Price):
        self.Price = Price

    def get_discount(self):
        return self.Discount
    def set_discount(self,Discount):
        self.Discount = Discount

    def get_stock(self):
        return self.Stock
    def set_stock(self,Stock):
        self.Stock = Stock