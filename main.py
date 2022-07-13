class Person(object):

    def __init__(self,name, id):
        self.name = name
        self.id =id
    def Diaplay(self):
        print(self.name, self.id)
emp = Person("akash",404)
emp.Diaplay()
class Emp(Person):
    def Print(self):
        print("Emp class called")
Emp_details = Emp("Akash", 201)
Emp_details.Diaplay()
Emp_details.Print()

class Person(object):

	def __init__(self, name):
		self.name = name
	def getName(self):
		return self.name

	def isEmployee(self):
		return False

class Employee(Person):
	def isEmployee(self):
		return True

emp = Person("Mr")
print(emp.getName(), emp.isEmployee())

emp = Employee("Mrs")
print(emp.getName(), emp.isEmployee())

class Person(object):
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post
		Person.__init__(self, name, idnumber)

a = Employee('Rifat', 1602060, 12000, "Intern")

a.display()
#for multiple inheritance

class Base1(object):
	def __init__(self):
		self.str1 = "Vivasoft"
		print("Base1")


class Base2(object):
	def __init__(self):
		self.str2 = "Limited"
		print("Base2")


class Derived(Base1, Base2):
	def __init__(self):

		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")

	def printStrs(self):
		print(self.str1, self.str2)


ob = Derived()
ob.printStrs()

###multilevel
class Base(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

class Child(Base):
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age
	def getAge(self):
		return self.age

class GrandChild(Child):
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address

	def getAddress(self):
		return self.address

g = GrandChild("Rifat", 26, "Vivasoft")
print(g.getName(), g.getAge(), g.getAddress())


