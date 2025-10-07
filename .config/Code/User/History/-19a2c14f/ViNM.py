# Design a hierarchy of classes all of which are programming languages. A programming language can be of 
# different types: Procedural, Object Oriented, Aspect Oriented, Functional, etc
# different programming languages are c, java, cpp
# C is procedural, Java is Object Oriented, CPP is both procedural and object oriented

# get_name()
# get_type()

class Languages:
    def get_name(self):
        print(self.name)
    
    def get_type(self):
        pass


class Procedural(Languages):
    def __init__(self):
        super().__init__()
    def get_type(self):
        return "Procedural"

class ObjectOriented(Languages):
    def __init__(self):
        super().__init__()
    
    def get_type(self):
        return "Object Oriented"
    
class AscpectOriented(Languages):
    def __init__(self):
        super().__init__()
    
    def get_type(self):
        return "AspectOriented"
    
class C(Procedural):
    def __init__(self):
        super().__init__()
    
    def get_name(self):
        return "C"
