#
# A simple program to identify grocery items that user wants to purchase
# Sales.py
#

__author__ = 'JohnHanlon'


class Cart:

    def __init__(self):
        ''' Initializiing Cart class

        Parameters
        ==========
        self : arg
            self argument

        Returns
        =======
        N/A : returns nothing
        '''

        self._contents = dict()

    def __repr__(self):
        ''' Dumps out the items in the cart, representation method

        Parameters
        ==========
        self : arg
            self arugment

        Returns
        =======
        Cart, self.__dict__ :
            the
        '''

        return '{0} {1}'.format(Cart, self.__dict__)

    def process(self, order):
        ''' Takes an order and adds or deletes

        Parameters
        ==========
        self : arg
            self argument
        order : str
            to which should be executed

        Returns
        =======
        N/A : returns nothing
        '''
        if order.add:
            if order.item not in self._contents:
                self._contents[order.item] = 0
            self._contents[order.item] += 1

        elif order.delete:
            if order.item in self._contents:
                self._contents[order.item] -= 1
                if self._contents[order.item] < 0:
                    del self._contents[order.item]


class Order:

    def __init__(self):
        ''' Initializing Order class

        Parameters
        ==========
        self : arg
            self argument

        Returns
        =======
        N/A : returns nothing
        '''

        self.quit = False
        self.add = False
        self.delete = False
        self.item = None

    def get_input(self):
        ''' Takes and returns an item

        Parameters
        ==========
        self : arg
            self argument

        Returns
        =======
        N/A : returns nothing
        '''

        print('[command] [item] (command is a to add, d to delete, q to quit)')
        line = input()

        command = line[:1]
        self.item = line[2:]

        if command == 'a':
            self.add = True

        elif command == 'd':
            self.delete = True

        elif command == 'q':
            self.quit = True


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
