import bicycles


# instantiate 6 bikes: model, weight in kilos and price in USD
bike1 = bicycles.Bicycle("mtx", 12, 120, 2)
bike2 = bicycles.Bicycle("city", 18, 165, 3)
bike3 = bicycles.Bicycle("ridex", 16, 200, 1)
bike4 = bicycles.Bicycle("mt2000", 12, 500, 5)
bike5 = bicycles.Bicycle("mt2200", 13, 1000, 3)
bike6 = bicycles.Bicycle("rvz100", 16, 2000, 3)

# instantiate a bike shop: name, margin, empty list as inventory and zero sales & profit
shop = bicycles.Shops("JoesBike", .20, [], 0, 0)
shop.populate_invetory([bike1, bike2, bike3, bike4, bike5, bike6], shop.inventory)

# instantiate 3 customers: name & budget
customer1 = bicycles.Customer("Mike", 200)
customer2 = bicycles.Customer("Sam", 500)
customer3 = bicycles.Customer("Alfred", 1000)

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