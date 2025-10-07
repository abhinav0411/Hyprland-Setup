# Design a hierarchy of classes all of which are programming languages. A programming language can be of 
# different types: Procedural, Object Oriented, Aspect Oriented, Functional, etc
# different programming languages are c, java, cpp
# C is procedural, Java is Object Oriented, CPP is both procedural and object oriented

# get_name()
# get_type()

class Languages:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        print(self.name)
    
    def get_type(self):
        pass

class Procedural(Languages):
    def __init__(self, name):
        super().__init__(name)
    
class ObjectOriented(Languages):
    def __init__(self, name):
        super().__init__(name)
    
class AscpectOriented(Languages):
    def __init__(self, name):
        super().__init__(name)
