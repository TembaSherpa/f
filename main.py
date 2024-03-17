# a = [{"name": "anil", "age": 8},
#      {"name": "sagar", "age": 10}
#     ]

# def validate_key(data):
#     required_keys = {'name', 'age'}
#     for d in data:
#         if not required_keys.issubset(d.keys()):
#             return False
#     return True

# print(validate_key(a))  



# def sum(a,b=12):
#     return a+b,2
# print(sum(2))

# def args_demo(*args):
#     sum=0
#     for arg in args:
#         sum+=arg
#     print(sum)
# args_demo(1,2,3,4)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def whoamI(self):
#         return self.name
# dog = Animal("dog")
# cat = Animal("cat")
# dog.whoamI()
# cat.whoamI()
# print(dog.whoamI())
# print(cat.whoamI())
# print(id(dog))

# class Chair:
#     def __init__(self, color):
#         self.color = color
#     def printColor(self):
#         print(f"the color is: {self.color}")
# red = Chair("red")
# white = Chair("white")
# red.printColor()
# white.printColor()


# class Color:
#     white = "#FFFF"
#     def __init__(self, color):
#         self.color = color
#     # Staticmethod
#     def printColor():
#         white = "#FFFF"
#         print(f"The color is {white}")

# Color.printColor()

# print(Color.white)

# class Calculator:
#     @staticmethod
#     def add(a, b):
#         return a + b
#     @staticmethod
#     def subtract(a, b):
#         return a - b
#     @staticmethod
#     def multiply(a, b):
#         return a * b
#     @staticmethod
#     def divide(a, b):
#         return a / b
    
# print(Calculator.add(10, 20))
# print(Calculator.subtract(10, 20))
# print(Calculator.multiply(10, 20))
# print(Calculator.divide(10, 20))

# class Animal:
#     def walk(self):
#         print("walking")
# #inheritance
# class Dog(Animal):
#     pass

# dog = Dog()
# dog.walk()

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def print_animal(self):
#         print(f"Hello {self.name}")

# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass
# dog = Dog("Robert")
# cat = Cat("Bob")

# dog.print_animal()
# cat.print_animal()

#polymorphism 
# class EncryptionKey:
#     PRIME_NUMBER = 11
#     def generate_key(self):
#         pass
# class RSA(EncryptionKey):
#     def generate_key(self):
#         return self.PRIME_NUMBER *2
    
# class AES(EncryptionKey):
#     def generate_key(self):
#         return self.PRIME_NUMBER *5

# def gen_key(encryption_class):
#     enc = encryption_class()
#     return enc.generate_key()

# print(gen_key(RSA))
# print(gen_key(AES))

#class method
class Encryption:
    PR = 11
    @classmethod
    def change_no(cls, new_no):
        cls.PR = new_no
    def change_num(self):
        self.PR = 50

class RSA(Encryption):
    def print_class_var(self):
        print(self.PR)

print(Encryption.PR)
Encryption.change_no(40)
print(Encryption.PR)

e = Encryption()
e.change_num()
print(e.PR)
RSA().print_class_var()


