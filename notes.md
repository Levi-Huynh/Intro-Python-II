TAKES NOTES FOR PURPOSE OF PARTICIPATE/INTERACT W/ YOUR LEARNING
-fast to participate
-but move more carefully & slowly to learn 
-learn as if you'll have to TL teach & troubleshoot/debug
-LEARN CS FOR PURPOSE OF TLING- MAKING A COMMIT TO SELF TO TL FOR CS #CALLED

OBJECT-ORIENTED DESIGN
-model real world or abstract concepts as objects
-MODEL OBJECTS W/ CLASSES
- classes normally repr as nouns

    -ATTRIBUTES- adjectives that describes our objects
    -METHODS - actions behaviors for our object
    -PROGRAMMING PARADIGM
    -EST RELATIONSHIPS BETWEEN OBJECTS

- CLASSES: USED TO MODEL *real world & abstract concepts as objects & define different relationships based on these objects* 
    -Blueprints to make multiple instances of same object
    -Can make multiple instances of an enemy class for a game, or
    animal class can have many instances
    - 2 main components
        -Attributes (values to describe the class object)
        -Methods- (verbs diff things our class can do)

-CLASS: -THINGS WE CAN REPRESENT AS NOUNS
- CLASS MODELING PLAYERS IN GAME
- MODELING ITEMS/ HEALTH KITS IN GAME
- ATTRIBUTES (ADJ THAT DESCRIBES OUR OBJECTS)
    GAME CLASS:
    -HEALTH
    -STRENGTH
    -SPEED

    ANIMAL CLASS:
    -NAME
    -HUNGER
    -DIET
-METHODS: (VERBS DESCRIBING OBJECTS)
    ANIMAL METHODS:
    -MOVE
    -EAT
    

-.STR helps describe class you're creating
OBJECT-ORIENTED DESIGN:
MODEL OBJECTS W/ CLASSES
-attributes
-methods
PROGRAMMING PARADIGM
ALLOWS US TO EST RELATIONSHIPS BETWEEN OBJECTS

-CONSTRUCTOR:
    -SPECIAL TYPE OF METHOD
    -GIVES OBJECTS *ATTRIBUTES* THEIR INTIAL VALUE
    -def__init() <-- in Python Constructor always has name __init()

    *SETTING ATTRIBUTES*
    class Animal:
    def__init(name, hunger, diet): //Method=def__init, (define init                                         method)
                                    // defining /list attributes
                                    //initial values taken in as params
    
    self.name = name                //assign params to actual attributes 
    self.hunger = hunger            //set class attribute (self.name) =                                    //to param  name
    self.diet = diet                //set class attribute (self.diet)
                                    //equal to diet param

    *SETTING METHODS*
    -One or more lines of code
    -defines specific behavior or action
    -may return a value
    -may have params
    def eat(self, food): // is self required here as param?
        if food>0 and hunger < 25:
            hunger +=food
    
-WHAT IS SELF? 
    -*SELF* indicates class-level variable (SCOPE IS ENTIRE CLASS)
    -Indicates changing or using the *CLASS* level attribute
    -Not variable just in method or block


SUMMARY:
Classes [nouns] used to model real-world objects
Think as blueprints to make multiple instances of same object
attributes [adjectives]
methods [verbs]]

Adventure Game TK VIDEO:
Characteristics:
-narrative-baed
-puzzles player asked to solve
-exploration
-text & graphic based
-colossal cave adventure 1976, text
-king's quest, zork I 1980, text & graphic
-monkey island 90, 93

Summary: 
-Type of narrative-based game that focuses on puzzles & exploration
Your job- implement a simple one with rooms that can be explored & items collected

TK SUMMARY:
Classes contain:

Fields - also known as attributes or properties. They hold state information about a specific instance of an object. Examples might include name, size, or image.

Methods - functions that belong to a specific class. They represent the behaviors this object should have. If we continue to think about the Player class, it might have methods such as move() or jump().

Constructors - special methods, defined with __init()__ in Python, that are used to instantiate an object of this class.

self - keyword used to refer to class-level variables and methods. These have scope across the entire class. Variables may also be declared normally and will have scope limited to the block of code they are declared within.