#
# A simple program to identify grocery items that user wants to purchase
# LTP - 05 - Shopping.py
#

__author__ = 'JohnHanlon'

import sales.shopping_cart
import sales.shopping_order

cart = sales.shopping_cart.Cart()
order = sales.shopping_order.Order()
order.get_input()

while not order.quit:
    cart.process(order)
    order = sales.shopping_order.Order()
    order.get_input()

print(cart)
