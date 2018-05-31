"""
SUMMARY: this module contains useful design patterns

In software engineering, a software design pattern is a general and reusable solution
to a commonly occuring problem within a given context in software design. it is not
a finished design that can be transformed directly into source or machine code.
It is a description or template for how to solve a problem that can be used in many
situations.  Design patterns are formalied best practices that the programmer can use
to solve common problmes when designing an application or system. 

Design patterns can speed up the development process by providing tested, proven
development paradigms. Effective software design requires considering issues that
may not become visible until later in the implementation. Freshly written code can
often have hidden subtle issues that take tie to be detected, issues that sometimes
can cause major problems down the road.  Reusing design patterns helps to prevent
such subtle issues, and also improves code readability for coders and architects
who are familiar with patterns.


DESIGN PATTERN CATEGORIES
	
	CREATIONAL
		- factory: creates objects dynamically
		- abstract factory: user expectation yields multiple, related objects
		- singleton: information cache (similar to global variables)
		- builder: removes need for objects with excessive number of constructors
		- prototype: crearting many identical objects 


	STRUCTURAL
		- decorator: add additional features dynamically without subclasses

	BEHAVIORAL

		Strategy: 

"""

""" factory """


# class Cat:
# 	""" A simple dog class"""
	
# 	def __init__(self, name):
# 		self.name = name

# 	def speak(self):
# 		return "Meow !"

# class Dog:
# 	""" A simple dog class"""
	
# 	def __init__(self, name):
# 		self.name = name

# 	def speak(self):
# 		return "Woof !"


# def get_pet(pet="dog"):
# 	""" The factory method used to create objects """
# 	pets = dict(dog=Dog('Hope'), cat=Cat('Peace'))
# 	return pets[pet]


# d = get_pet('dog')
# print(d.speak())

# c = get_pet('cat')
# print(c.speak())


""" abstract factory """

# class Dog:

# 	def speak(self):
# 		return 'Woof!'

# 	def __str__(self):
# 		return "Dog"


# #Concrete factory
# class DogFactory:

# 	def get_pet(self):
# 		""" Returns a dog object """
# 		return Dog()

# 	def get_food(self):
# 		""" Regurn a dog food object """
# 		return "Dog Food !"


# class PetStore:

# 	""" Pet store is an abstract factory """
# 	def __init__(self, pet_factory=None):
# 		self._pet_factory = pet_factory

# 	def show_pet(self):
# 		""" Unitity method to display detailed of the object returned by the DogFactory"""
# 		pet = self._pet_factory.get_pet()
# 		pet_food = self._pet_factory.get_food()

# 		print("Our pet is {}".format(pet))
# 		print("Our pet says hello by {}".format(pet.speak()))
# 		print("Its food is {}".format(pet_food))



# # Create a concrete factory
# factory = DogFactory()

# #Create a pet sotre housing our abstract factory
# shop = PetStore(factory)

# shop.show_pet()


""" singleton """

# class Borg:
# 	""" Borg class making class attributes global """
# 	_shared_state = {}
	
# 	def __init__(self):
# 		#Making an attribute dictionary
# 		self.__dict__ = self._shared_state

# class Singleton(Borg): #inherits from the Borg class

# 	def __init__(self, **kwargs):
# 		#Update our attribute dictionary by inserting a new key-value paier 
# 		Borg.__init__(self)
# 		self._shared_state.update(kwargs)

# 	def __str__(self):
# 		#Returns the attribute dictionary for printing
# 		return str(self._shared_state)

# #Let's create a singleton object and add our first acronym
# x = Singleton(HTTP = 'Hyper Text Transfer Protocol')

# #Print the object
# print(x)

# #Lets create another singleton object and if it refers to the same attribution dictionary by adding acronym
# y = Singleton(SNMP = "Single Network Management Protocol")
# #print the object - can see multiple files
# print(y)


""" builder """


# class Director():
# 	""" Director """
# 	def __init__(self, builder):
# 		self._builder = builder

# 	def construct_car(self):
# 		self._builder.create_new_car()
# 		self._builder.add_model()
# 		self._builder.add_engine()
# 		pass

# 	def get_car(self):
# 		return self._builder.car


# class Builder():
# 	""" Abstract Buildeer """
# 	def __init__(self):
# 		self.car = None

# 	def create_new_car(self):
# 		self.car = Car()


# class SkylarkBuilder(Builder):
# 	""" Concrete Builder: provides parts adn tools to work on the parts """
	
# 	def add_model(self):
# 		self.car.model = 'Skylark'

# 	def add_tires(self):
# 		self.car.tires = 'Regular tires'

# 	def add_engine(self):
# 		self.car.engine = 'Turbo engine'


# class Car():
# 	""" Product """
# 	def __init__(self):
# 		self.model = None
# 		self.tires = None
# 		self.engine = None

# 	def __str__(self):
# 		return "{} | {} | {}.".format(self.model, self.tires, self.engine)
# 	pass 


# builder = SkylarkBuilder()
# director = Director(builder)
# director.construct_car()
# car = director.get_car()

# print(car)


""" prototype """

# import copy

# class Prototype:

# 	def __init__(self):
# 		self._objects = {}

# 	def register_object(self, name, obj):
# 		""" Register object """
# 		self._objects[name] = obj

# 	def unregister_object(self, name):
# 		del self._objects[name]

# 	def clone(self, name, **attr):
# 		obj = copy.deepcopy(self._objects.get(name))
# 		obj.__dict__.update(attr)
# 		return obj

# class Car:
# 	def __init__(self):
# 		self.name = 'skylark'
# 		self.color = 'color'
# 		self.options = 'ex'

# 	def __str__(self):
# 		return "{} | {} | {}".format(self.name, self.color, self.options)

# c = Car()
# prototype = Prototype()
# prototype.register_object('skylark', c)

# c1 = prototype.clone('skylark')

# print(c1)





