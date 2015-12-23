class Bicycle(object):
    def __init__(self, model, weight, cost, stock):
        self.model = model
        self.weight = weight
        self.cost = cost
        self.stock = stock

class Shops(object):
    def __init__(self, name, margin, inventory, sales, profits):
        self.name = name
        self.margin = margin
        self.inventory = inventory
        self.sales = sales
        self.profits = profits
    
    def populate_invetory(self, bike_list = [], inventory = []):
        # adds indivudlal bike models to shop inventory (which is a list of obejcts)
        for each in range(len(bike_list)):
            inventory.append(bike_list[each])

    def print_inventory(self, inventory):
        # prints all details of current inventory
        print()
        for i in inventory:
            print("Model: {} Weight: {}kg Cost: ${} In Stock: {} Retail Price: ${:.2f}".format(i.model, i.weight, i.cost, i.stock, i.cost / (1 - self.margin)))
    
    def sell_bike(self, model, inventory = []):
        # loop through inventory to find right model
        for i in range(len(inventory)):
            if inventory[i].model == model:    # once right model is found...
                if inventory[i].stock > 0:     # make sure it's in stock
                    inventory[i].stock -= 1                # substract from stock
                    self.sales += (inventory[i].cost / (1 - self.margin))       # add retail price to sales
                    self.profits += ((inventory[i].cost / (1 - self.margin)) - inventory[i].cost)         # add difference between price and cost to profits
                    print("One model {} bicycle sold for ${:.2f}!".format(model, (inventory[i].cost / (1 - self.margin))))
                else:
                    print("No stock left for model {}".format(model))
    
    def results(self):
        print()
        print("Total sales: {}".format(self.sales))
        print("Total profits: {}".format(self.profits))

class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
    
    def can_buy(self, shop, inventory = []):
        print()
        # print customer details
        print("{} has a budget of ${} and can afford the following bikes:".format(self.name, self.budget))
        # loop over inventory and compare budget to retail price, only list bikes below budget
        for i in inventory:
            if self.budget >= (i.cost / (1 - shop.margin)) :
                print("Bike model: {} for ${:.2f}: {} in stock.".format(i.model, (i.cost / (1 - shop.margin)), i.stock)) 
    
    def buy(self, model, shop, inventory = []):
        print()
        # loop over inventory to find right model
        for x in inventory:
            if x.model == model:            # once right model is found...
                if x.stock > 0:             # make sure it's in stock
                    if self.budget >= (x.cost / (1 - shop.margin)):     # then make sure its retail price is below customer budget
                        self.budget -= (x.cost / (1 - shop.margin))     # substract retail pruce from customer budget
                        print("{} bought a {} bike for ${:.2f} and has ${:.2f} left.".format(self.name, model, (x.cost / (1 - shop.margin)), self.budget))
                    else:
                        print("Sorry {}, too expensive.".format(self.name))
                else:
                    print("Sorry, that model is out of stock.")



# Code implementation ------------------------------

# instantiate 6 bikes: model, weight in kilos and price in USD
bike1 = Bicycle("mtx", 12, 120, 2)
bike2 = Bicycle("city", 18, 165, 3)
bike3 = Bicycle("ridex", 16, 200, 1)
bike4 = Bicycle("mt2000", 12, 500, 5)
bike5 = Bicycle("mt2200", 13, 1000, 3)
bike6 = Bicycle("rvz100", 16, 2000, 3)

# instantiate a bike shop: name, margin, empty list as inventory and zero sales & profit
shop = Shops("JoesBike", .20, [], 0, 0)
shop.populate_invetory([bike1, bike2, bike3, bike4, bike5, bike6], shop.inventory)

# instantiate 3 customers: name & budget
customer1 = Customer("Mike", 200)
customer2 = Customer("Sam", 500)
customer3 = Customer("Alfred", 1000)

# print bike inventory
shop.print_inventory(shop.inventory)

# print names of customers and the bike models they can purchase give their budget
customer1.can_buy(shop, shop.inventory)
customer2.can_buy(shop, shop.inventory)
customer3.can_buy(shop, shop.inventory)

# customers purchase a bike and shop sells a bike
customer1.buy("mtx", shop, shop.inventory)
shop.sell_bike("mtx", shop.inventory)

customer2.buy("ridex", shop, shop.inventory)
shop.sell_bike("ridex", shop.inventory)

customer3.buy("mt2000", shop, shop.inventory)
shop.sell_bike("mt2000", shop.inventory)

# print final inventory and sales and profits
shop.print_inventory(shop.inventory)
shop.results()

