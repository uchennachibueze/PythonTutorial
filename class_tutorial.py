'''
    Showing difference between class variables and instance variables
'''
# class Dog:
#     kind = 'canine' # class variable

#     def __init__(self, name):
#         self.name = name


class Dog:
    # tricks = [] # Not good as other instances of the classes or object may use data that does not apply to them

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

        
        