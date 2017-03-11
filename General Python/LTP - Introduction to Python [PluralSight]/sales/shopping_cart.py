#
# A simple program to work with the user's shopping cart
# shopping_cart.py
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
                    