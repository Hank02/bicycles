class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

class Shops(object):
    def __init__(self, name, margin, inventory, sales, profits):
        self.name = name
        self.margin = margin
        self.inventory = inventory
        self.sales = sales
        self.profits = profits
    
    def populate_invetory(self, bike_list = [], inventory = []):
        # adds indivudlal bike models to shop inventory (which is a list of lists)
        for each in range(len(bike_list)):
            # append each model's characteristics to a list and the append that list to inventory
            sku = []
            sku.append(bike_list[each].model)
            sku.append(bike_list[each].weight)
            sku.append(bike_list[each].cost)
            sku.append(int(input("Enter quantity of {}: ".format(bike_list[each].model))))
            sku.append(bike_list[each].cost / (1 - self.margin))
            inventory.append(sku)
    
    def print_inventory(self, inventory):
        # prints all details of current inventory
        print("\n")
        for each in inventory:
            print("Model: {} Weight: {}kg Cost: ${} In Stock: {} Retail Price: ${:.2f}".format(each[0], each[1], each[2], each[3], each[4]))
    
    
    def sell_bike(self, model, inventory = []):
        # loop through inventory to find right model
        for i in range(len(inventory)):
            if inventory[i][0] == model:    # once right model is found...
                if inventory[i][3] > 0:     # make sure it's in stock
                    inventory[i][3] -= 1                # substract from stock
                    self.sales += inventory[i][4]       # add retail price to sales
                    self.profits += (inventory[i][4] - inventory[i][2])         # add difference between price and cost to profits
                    print("One model {} bicycle sold for ${:.2f}!".format(model, inventory[i][4]))
                else:
                    print("No stock left for model {}".format(model))
    
    def results(self):
        print("\n")
        print("Total sales: {}".format(self.sales))
        print("Total profits: {}".format(self.profits))

class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
    
    def can_buy(self, inventory = []):
        print("\n")
        # print customer details
        print("{} has a budget of ${} and can afford the following bikes:".format(self.name, self.budget))
        # loop over inventory and compare budget to retail price, only list bikes below budget
        for i in range(len(inventory)):
            if self.budget >= inventory[i][4]:
                print("Bike model: {} for ${:.2f}: {} in stock.".format(inventory[i][0], inventory[i][4], inventory[i][3])) 
    
    def buy(self, model, inventory = []):
        print("\n")
        # loop over inventory to find right model
        for x in range(len(inventory)):
            if inventory[x][0] == model:            # once right model is found...
                if inventory[x][3] > 0:             # make sure it's in stock
                    if self.budget >= int(inventory[x][4]):     # then make sure its retail price is below customer budget
                        self.budget -= int(inventory[x][4])     # substract retail pruce from customer budget
                        print("{} bought a {} bike for ${:.2f} and has ${:.2f} left.".format(self.name, model, inventory[x][4], self.budget))
                        break
                    else:
                        print("Sorry {}, too expensive.".format(self.name))
                        break
                else:
                    print("Sorry, that model is out of stock.")
                    break





# Code implementation ------------------------------

# instantiate 6 bikes: model, weight in kilos and price in USD
bike1 = Bicycle("mtx", 12, 120)
bike2 = Bicycle("city", 18, 165)
bike3 = Bicycle("ridex", 16, 200)
bike4 = Bicycle("mt2000", 12, 500)
bike5 = Bicycle("mt2200", 13, 1000)
bike6 = Bicycle("rvz100", 16, 2000)

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
customer1.can_buy(shop.inventory)
customer2.can_buy(shop.inventory)
customer3.can_buy(shop.inventory)

# customers purchase a bike and shop sells a bike
customer1.buy("mtx", shop.inventory)
shop.sell_bike("mtx", shop.inventory)

customer2.buy("ridex", shop.inventory)
shop.sell_bike("ridex", shop.inventory)

customer3.buy("mt2000", shop.inventory)
shop.sell_bike("mt2000", shop.inventory)

# print final inventory and sales and profits
shop.print_inventory(shop.inventory)
shop.results()

