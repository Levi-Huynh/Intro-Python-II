
OOP CORE CONCEPTS
INHERITANCE-  Allow us to define heirarchical relationships bewteen different Classes 
                -Appropriate method overriding  & use of super()
ASSOCIATION- Objects thare refer to other objects 
                -appropriate class design

Benefits: avoid typing redundant code- right it once, and never gain

-Python supports multiple inheritance- child cam inherit from multiple parent classes (not true for all lang)
- -IF CHILD EXTENDING FROM PARENT-
    -CAN JUST WRITE ATTRIBUTES UNIQUE TO DOG CLASS (parent classes included)
    - AND INCLUDE WHAT MAKES SENSE FOR THAT CHILD SPECIFIC TO THAT CHILD(DOG = FETCH)



# Child classes can also override parent methods to define alternate or additional behaviors. Inheritance is also sometimes described as an “is-a” relationship.

# Inheritance relationships can be defined between classes in situations where more specific child classes extend the functionality of more general parent classes.

# Method overriding - ```used if a child class needs to `function slightly differently than objects of the parent class`. Method overriding is done by giving the child class a method with the same name as one found in the parent. This method will then be called in lieu of the one defined in the parent class.```

# super() - a keyword that can be used to reference methods or constructors from the parent class. It is often used when ...overriding methods.

# ASSOCIATIONS: "has a": We need another way to describe relationships that are more accurately described as “has-a” relationships. In object-oriented design, these relationships are known as associations.

# book would never be "is a" relationship to author.. but a "has a" relationship
    - no inheritance (not "is a")
    - is association ("has a")
    -Author is attribute in our `Book` Class

    `class Book:
    def __init__( self, name, year, author_first, author_last ):
 	self.name = name
        self.year = year
	self.author = Author( author_first, author_last )
    # class functions would be added here `

`class Author:
    def __init__( self, first, last ):
 	self.first = first
        self.last = last
        # class functions would be added here  `

What is an example of two classes that would be related through composition? rest-waiter, store-casher
What is an example of two classes that would be related through aggregation? menu-drink, 

? Syntax wise Composition & Aggregation set up the same-- attribute from class A are instances of class B?
or ...Using a custom class when creating attributes of another custom class




2/19 TK NOTES
- Animal 
FIsh  Mammal
       Cat   Dog

Animal here is most general can have many subgroups. 
-Can avoid re writing common attributes/methods
-Python supports multiple inheritance 
-if dog inheriting from parent class, only write things unique to dog (breed, indoor/outdoor, fetch method)
^ CHILD CLASS is LARGER THAN PARENT CLASS (PARENT CLASS IS SMALLEST CLASS) (Has parents & own attributes/methods)
-When want to use attributes & methods from Parent class: 
    -MUST LIST THE PARENT ATTRIBUTES IN def__init__
    -mULST LIST JUST THE PARENT ATTIBUTES IN  super()__init__  ***MEANS CALL CONSTRUCTOR IN PARENT/ANIMAL CLASS & INITILIZE THOSE ATTRIBUTES***  # Is Method Overriding #  

- dog has access to parent attributes if an instance of parent, but can override those methods (use the same method name?) & write conditions/functions specific to the child for that method 

Parent class (aka called Super class )
Child class (aka subclass)


# Child classes can also override parent methods to define alternate or additional behaviors. Inheritance is also sometimes described as an “is-a” relationship.

# ASSOCIATIONS: "has a": We need another way to describe relationships that are more accurately described as “has-a” relationships. In object-oriented design, these relationships are known as associations.

# Inheritance relationships can be defined between classes in situations where more specific child classes extend the functionality of more general parent classes.

# Method overriding - ```used if a child class needs to `function slightly differently than objects of the parent class`. Method overriding is done by giving the child class a method with the same name as one found in the parent. This method will then be called in lieu of the one defined in the parent class.```

# super() - a keyword that can be used to reference methods or constructors from the parent class. It is often used when ...overriding methods.


# book would never be "is a" relationship to author.. but a "has a" relationship

INHERIT:
parent/child
type/sub type
is-a

ASSOC:
has-a 
link between 2 classes
Composition:
    -class A CANT exist w/out class B
        -restuarnt -> has a menu, employee

Aggregation:
    -class A CAN exist independently of class B
        -menu ->  drink, food


Ex Assoc:

class Resaurant:
    def __init__(self, name, staff, dinner_menu)
    self.name = name
"has an"    self.staff = Employee[]
"has an"    self.dinner_menu = Menu()

^^ Association relationships between classe can be: We can define attributes in class A that are instances of class B