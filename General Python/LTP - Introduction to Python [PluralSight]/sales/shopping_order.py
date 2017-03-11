#
# A simple program to place an order in a shopping cart
# order.py
#

__author__ = 'JohnHanlon'

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
