class Bicycle(object):
    def __init__(self, model_name, weight, cost):
        self.model_name = model_name
        self.weight = weight
        self.cost = cost
        
class BikeShop(object):
    def __init__ (self, shop_name, bicycle_inventory = {}, bicycle_markup = 0.0):
        self.shop_name = shop_name
        self.bicycle_inventory = bicycle_inventory
        self.bicycle_markup = bicycle_markup
        self.profit_balance = 0
        
    #calculate sale price for bicycle"
    def bicycle_sales_price(self, bicycle):
        return int(bicycle.cost + round(bicycle.cost * self.bicycle_markup,0))
        
    #Print inventory of bicycles with an optional price limit
    #I would like to go over this function and understand the flow of parameters
    def print_inventory(self, sale_price_limit = 9999):
        print ("Name    Count   Sales Price")
        for bicycle in self.bicycle_inventory:
            bicycle_sale_price = self.bicycle_sales_price(bicycle)
            if bicycle_sale_price < sale_price_limit:
                print("{}    {}     ${}".format(bicycle.model_name, self.bicycle_inventory[bicycle], bicycle_sale_price))
    
    #Sell bicycle
    def sell_bicycle(self, bicycle):
        if self.bicycle_inventory[bicycle] > 0:
            bicycle_profit = self.bicycle_sales_price(bicycle) - bicycle.cost
            self.profit_balance += bicycle_profit
            self.bicycle_inventory[bicycle] -= 1
            print ("{} has successfully sold a {} for ${}.".format(self.shop_name, bicycle.model_name,bicycle_profit))
            
    
class Customer(object):
    def __init__ (self, customer_name, bicycle_fund, bicycle = None):
        self.customer_name = customer_name
        self.bicycle_fund = bicycle_fund
        self.bicycle = bicycle
        
    #Customer purchases bicycle and reduces bicycle fund    
    def purchase_bicycle(self, bicycle, bicycle_cost):
        self.bicycle = bicycle
        self.bicycle_fund -= bicycle_cost
        print ("Congratulations {}, you have purchased a {} for ${}. You have ${} remaining of your bicycle fund".format(self.customer_name, bicycle.model_name, bicycle.cost, self.bicycle_fund))