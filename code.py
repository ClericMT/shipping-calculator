import math

stock_list = []
receipt_num = 0000

class Stock:
    def __init__(self, name, code, bundle_sizes):
        self.name = name
        self.code = code
        self.bundle_sizes = bundle_sizes
        self.num_of_stock = 0
        self.total_order = {}
        self.total_price = 0

    def num_of_bundles(self):
        bundles = (sorted(self.bundle_sizes.keys(), reverse = True)) #Sorts available bundle sizes from highest (least bundle_sizes required) to lowest
        items_left = self.num_of_stock #Remainder of items to bundle
        for bundle in range(len(bundles)): #Compute how much stock can be bundled in the available sizes (from highest available size -> lowest available size)
            keys_list = list(bundles)
            num_of_bundle = (math.floor(items_left/bundles[bundle]))
            items_left = self.num_of_stock - (bundles[bundle] * num_of_bundle)
            self.total_order[num_of_bundle] = {keys_list[bundle]: self.bundle_sizes[bundles[bundle]]} #Adds bundles to total_order list
            self.total_price += self.bundle_sizes[bundles[bundle]] * num_of_bundle #Updates total price
        self.print_total_order()

    def print_total_order(self): #Format strings for legibility and log
        if self.num_of_stock != 0:
            print(' ' + str(self.num_of_stock) + ' ' + str(self.code) + ' $' + str("{:.2f}".format(self.total_price)))
            for bund_size, bund_info in self.total_order.items():
                if bund_size != 0:
                    for key in bund_info:
                        print('     ' + str(bund_size) + ' x ' + str(key) + ' $' + str(bund_info[key]))

vegemite_scroll = Stock('Vegemite Scroll', 'VS5', {3: 6.99, 5: 8.99}) #Creates new stock items
blueberry_muffin = Stock('Blueberry Muffin', 'MB11', {2: 9.95, 5: 16.95, 8: 24.95})
croissant = Stock('Croissant', 'CF', {3: 5.95, 5: 9.95, 9: 16.99})
stock_list.extend([vegemite_scroll, blueberry_muffin, croissant]) #Appends to stock list ###Could also create an appendix?

while True: #Menu
    user_input = input('\n1. Add to order\n2. Finalise order\n3. Appendix\n')
    if user_input == '1':
        num_of_stock, item_code = input("Enter stock code: ").split()
        for item in stock_list:
            if item_code == item.code:
                item.num_of_stock += int(num_of_stock)
    elif user_input == '2':
        print('\nOR#' + str("{0:0=8d}".format(receipt_num)))
        for stock in stock_list:
            stock.num_of_bundles()
            stock.total_order.clear() #Reset stock list for next order
            stock.total_price = 0
            stock.num_of_stock = 0
        receipt_num += 1
    elif user_input == '3':
        for stock in stock_list:
            print(stock.name + ': ' + stock.code)


