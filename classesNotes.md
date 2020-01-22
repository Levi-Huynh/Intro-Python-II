Nouns- Not all nouns will be classes

Verbs- Methods
class blue print for object

class Store: 
	def__init__(self, name): 
		self.name = name 

#? why is self listed as param in python (this isn't a param)
#constructor. Self => this ==self (refers to obj 
#being constructed, equal to this or binding, need
#instance . telling the class whats being constructed
		print("constructor was called")
		print(self) #<__main__.Store object at 0x105a49eb8> main is file, Store
					#class called in that file 
		def__str__(self):
			return f"Store: {self.name}"  #__str__ will return self object
										#& be useless unless we create fstring
									#as it will print out anything there unless
									#we create something useful
	
myStore = Store() #create new store object
print(myStore) #<__main__.Store object at 0x105a49eb8> main is file, Store
					#class called in that file (same as print(self))
				#b/c of the def __str__(self) returning useful info
					#when def __str__(self): 
					#returns self.name, f string is useful (print(myStore))
				? self can be passed in def __str__(self) : & not used
					but would still print if that store instance with whatever
								returned.  def_method(self) do something same?
			def __repr__(self):
				return f'Store("' + self.name + '")'
			# repr program string with python code to make/recreate the object
            # print(repr(myStore)) // Store("Beej's Store")
            # __str__(self): // Store: Beej's Store 

															
#will error out without positional arg name

#repl ==> type name of object will be weird unless have
repr defined
repr shows you how to recreate==> good form to have in your class
so that it shows other devs how to recreate
repr (developer programmer friendly version of __str__ how is this thing recreated, this object recreated. should return python
code to construct that object0

PYTHON DOESN'T SUPPORT HOISTING

																

https://www.w3schools.com/python/python_inheritance.asp