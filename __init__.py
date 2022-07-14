
class Person:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('Hello, my name is', self.name)

	def say_hlw(self):
		print('I am from', self.name)

p1 = Person('Rifat')
p2 = Person('mahmud')
p3 = Person('akash')
p4 = Person('Vivasoft')
p1.say_hi()
p2.say_hi()
p3.say_hi()
p4.say_hlw()

### inheritance for init constructor

class A(object):
	def __init__(self, something):
		print("A class init is called")
		self.something = something


class B(A):
	def __init__(self, something):
		A.__init__(self, something)
		print("B init is called")
		self.something = something

obj = B("Something")

class A(object):
	def __init__(self, something):
		print("A init called")
		self.something = something

class B(A):
	def __init__(self, something):
		print("B init called")
		self.something = something
		A.__init__(self, something)


obj = B("Something")

#__str__
##__rpr__
#__call__
#__add__


class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString
    def __str__ (self):
        return 'MyClass(x=' + str(self.x) + ' ,y=' + self.y + ')'
myObject = MyClass(12345, "hallo vivasoft")

print(myObject.__str__())
print(myObject)
print(str(myObject))
print(myObject.__repr__())

class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString
    def __repr__ (self):
        return 'MyClass(x=' + str(self.x) + ' ,y=' + self.y + ')'
myObject = MyClass(12345, "Hello bro")

print(myObject.__str__())
print(myObject)
print(str(myObject))
print(myObject.__repr__())


class Example:
    def __init__(self):
        print("Instance Created")

    def __call__(self):
        print("Instance is called via special method")


e = Example()

e()

class Product:
	def __init__(self):
		print("Instance Created")

	def __call__(self, a, b):
		print(a * b)

ans = Product()

ans(10, 20)


class Data:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Data(self.value + other.value)


a = Data(40)
b = Data(2)
c = a + b

print(c.value)

