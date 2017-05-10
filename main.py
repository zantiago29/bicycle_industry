from bicycles import Bicycle, BikeShop, Customer
        
#Create 6 bicycle models
bicycle1 = Bicycle("Mongoose", 500, 50)
bicycle2 = Bicycle("Ascent", 490, 100)
bicycle3 = Bicycle("Bern", 480, 150)
bicycle4 = Bicycle("Charge", 450, 400)
bicycle5 = Bicycle("Brooks", 430, 600)
bicycle6 = Bicycle("Bodyglide", 200, 1500)

#Create bicycle shop with 6 models in stock and 20% markup
bicycleshop1 = BikeShop("Bicycle World", {bicycle1: 100, bicycle2: 100, bicycle3: 100, bicycle4: 100, bicycle5: 100, bicycle6: 100}, .20)

#Create 3 customers
customer1 = Customer("Frank", 200)
customer2 = Customer("Dan", 500)
customer3 = Customer("Sergio", 1000)
customers = [customer1, customer2, customer3]

#Print list of customer and the bikes they can afford
for customer in customers:
    print ("{} Current Inventory for {}".format(bicycleshop1.shop_name, customer.customer_name)) #how are the brackets being used here?
    bicycleshop1.print_inventory(customer.bicycle_fund)
    print("")
    
print ("{} total starting inventory".format(bicycleshop1.shop_name))
bicycleshop1.print_inventory()
print ("")

bicycle_purchases = {customer1: bicycle1, customer2: bicycle2, customer3: bicycle3}
print ("Bicycle Purchases")
for customer in bicycle_purchases:
  bicycle_sold = bicycle_purchases[customer]
  customer.purchase_bicycle(bicycle_sold, bicycleshop1.bicycle_sales_price(bicycle_sold))
  bicycleshop1.sell_bicycle(bicycle_sold)
  print ("")
    
print ("{} total ending inventory".format(bicycleshop1.shop_name))
bicycleshop1.print_inventory()
print ("")
print ("{} Total Profit = ${}".format(bicycleshop1.shop_name, bicycleshop1.profit_balance))
    
    


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        