# @property, @staticmethod, @classmethod

class Animal:
    def __init__(self, kind, size):
        self._kind = kind   # _ before the field name = private
        self.size = size

    @property
    def kind(self): # works as a getter
        return self._kind

    @kind.setter
    def kind(self, kind):   # setter
        if isinstance(kind, str):
            self._kind = kind
        else:
            raise TypeError("str expected")

class Math:
    @staticmethod   # static method
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

class Person:
    kind = "Homosapiens"

    @classmethod    # class method (only accesses class fields and methods)
    def get_kind(cls):
        return cls.kind

animal = Animal("cat", "big")
print(animal.kind)

m = Math()
m.add(1, 2)

person = Person
print(person.get_kind())