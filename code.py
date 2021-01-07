#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

#Stock items
VS5 = {3: 6.99, 5: 8.99}
MB11 = {2: 9.95, 5: 16.95, 8: 24.95}
CF = {3: 5.95, 5: 9.95, 9: 16.99}

#List of stock
items = {"VS5": VS5,"MB11": MB11,"CF": CF}

def calculate_price(amount, stock):
    total_price = 0
    r = amount #remainder
    order = []
    iter_items = sorted([k for k in items[stock]], reverse = True) #grabs available bundle sizes
    for x in range(len(iter_items)):
        b = math.floor(r / iter_items[x]) #amount of bundle
        r = r - (b * iter_items[x]) #update remainder stock
        order.append(b) #update order
        total_price += items[stock][iter_items[x]] * b
    print(str(amount) + ' ' + str(stock) + ' $' + str("{:.2f}".format(total_price)))
    for x in range(len(iter_items)):
        if order[x] > 0:
            print('     ' + str(order[x]) + ' x ' + str(iter_items[x]) + ' $' + str(items[stock][iter_items[x]]))

if __name__ == "__main__":
    calculate_price(10, "VS5")
    calculate_price(14, "MB11")
    calculate_price(13, "CF")
