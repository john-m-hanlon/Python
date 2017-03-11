#
# A simple program to identify grocery items that user wants to purchase
# LTP - 03 - Data Structures.py
#

__author__ = 'JohnHanlon'


def get_order():
    ''' Takes and returns an item

    Parameters
    ==========
    N/A : takes no parameters

    Returns
    =======
    command : str
        the action provided by the user
    item : str
        the item provided by the user
    '''

    print('[command] [item] (command is a to add, d to delete, q to quit)')
    line = input()
    command = line[:1]
    item = line[2:]
    return command, item


def add_to_cart(item, cart):
    ''' adds an item to your cart

    Parameters
    ==========
    item : str
        the item which will be added to the cart
    cart : dict
        diction of the items currently held

    Returns
    =======

    '''

    if item not in cart:
        cart[item] = 0
    cart[item] += 1


def delete_from_cart(item, cart):
    ''' removes an item from the cart

    Parameters
    ==========
    item : str
        the item which will be removed from the cart
    cart : dict
        dictioanry of the items currently held

    Returns
    =======

    '''

    if item in cart:
        cart[item] -= 1


def process_order(order, cart):
    ''' unpacks the order

    Parameters
    ==========
    order : str
        the action provided by the user
    cart : str
        the cart available to the user

    Returns
    =======
    True : boolean
        Allows us to end the loop after a user quits ordering
    '''

    command, item = order

    if command == 'a':
        add_to_cart(item, cart)

    elif command == 'd' and item in cart:
        delete_from_cart(item, cart)

    elif command == 'q':
        return False

    return True


def go_shopping():
    ''' Provides a list of items in our shopping cart that starts off as empty

    Parameters
    ==========
    N/A : takes no parameters

    Returns
    =======


    '''

    cart = dict()
    while True:
        order = get_order()
        if not process_order(order, cart):
            break

    print(cart)
    print('Finished!')


go_shopping()
