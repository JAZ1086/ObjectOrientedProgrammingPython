class ParentClass:
    def call_me(self):
        print("I'm parent class")

class ChildClass:
    def call_me(self):
        print("I'm a child class")


pobj  = ParentClass()
pobj.call_me()

cobj = ChildClass()
cobj.call_me()

