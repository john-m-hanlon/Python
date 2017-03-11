#
# A simple program to identify grocery items that user wants to purchase
# LTP - 04 - Concepts of Object Oriented Programming.py
#

__author__ = 'JohnHanlon'


class Classroom:

    def __init__(self):
        '''Initializing class

        Parameters
        ==========
        self : arg
            self argument

        Returns
        =======
        N/A : returns nothing
        '''
        self._people = []

    def add_person(self, person):
        ''' Adds person to the classroom

        Parameters
        ==========
        self : arg
            self argument
        person : str
            person who is being added into the classroom

        Returns
        =======
        N/A : returns nothing
        '''

        self._people.append(person)

    def remove_person(self, person):
        ''' Removes person from the classroom

        Parameters
        ==========
        self : arg
            self argument
        person : str
            person who is being removed from the class room

        Returns
        =======
        N/A : returns nothing
        '''

        self._people.remove(person)

    def greet(self):
        ''' Want to loop through each person in the room and say hello

        Parameters
        ==========
        self : arg
            self argument

        Returns
        =======
        N/A : returns nothing
        '''

        for person in self._people:
            person.say_hello()


class Person:

    def __init__(self, name):
        ''' Initiatializing class

        Parameters
        ==========
        self : arg
            self argument

        name : str
            Name of the parameter called from the class and passed inito Init

        Returns
        =======
        N/A : returns nothing
        '''

        self.name = name

    def say_hello(self):
        ''' Says hello to the person

        Parameters
        ==========
        self : arg
            self argument

        Returns
        =======
        N/A : returns nothing
        '''

        print(id(self))
        print('Hello! {}'.format(self.name))

# Instantiation


# p1 = Person('Scott')
# p2 = Person('Alex')
# print(id(p1))
# print(id(p2))
# p1.say_hello()

room = Classroom()
room.add_person(Person('John'))
room.add_person(Person('Michael'))
room.add_person(Person('Hanlon'))

room.greet()


