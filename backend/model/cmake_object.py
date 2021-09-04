
# immutable representation of a key on the CmakeObject
class Ckey():
    def __init__(name : String):
        self.name = name
    def name():
        return self.name

# a cmake object represented in our code
class CmakeObject():
    def __init__(self):
        self.children = [] # cmake objects below
        self.parent = None # cmake object above
    # return self
    def self(self):
        return self
    # Monoid
    # to consume an object is to take it and child it
    # to this object
    def consume(self, other_cmake_object : CmakeObject):
        return self
    # Monoid
    # to combine this object to another object is to take
    # that object and create an owning relationship with
    # this one
    def combine(self, other_cmake_object : CmakeObject):
        return self
    # to JSON
    def json(self):
        return self
    # map function over all values
    def map(self, function):
        return self

# create a view to the CmakeObject cmake_object with key
# string name
def view(cmake_object : CmakeObject, key : String):
    return cmake_object