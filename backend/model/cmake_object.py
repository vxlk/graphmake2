
# immutable representation of a key on the CmakeObject
class Ckey():
    def __init__(self, name : String):
        self.name = name
    def name(self):
        return self.name

# a directory
class DirectoryObject():
    def __init__(self, path):
        self._path = path
        self._subdirs = []
        self._targets = []

class SymbolTable():
    def __init__(self) -> None:
        self._targets = []
        self._unused_symbols = []

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
    # to this object - making this object the new owner
    def consume(self, other_cmake_object : CmakeObject) -> CmakeObject:
        return self
    # Monoid
    # to combine this object to another object is to take
    # that object and create a sibling relationship with the parent
    def combine(self, other_cmake_object : CmakeObject) -> CmakeObject:
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


# The data model will consume
# directories
# 1st order objects
# 2nd order objects
# 1st order objects are composed of 1st order objects and 2nd order objects
# 2nd order objects are strings
#
# Examples of first order objects
# targets
# Examples of 2nd order objects
# properties on a target