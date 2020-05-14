""" 1) Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, 
color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable 
testTwo an instance of Bike whose color is purple and whose price is 25.0.
"""

class Bike():
    
    def __init__(self, colorString, priceFloat):
        self.color = colorString
        self.price = priceFloat
    
testOne = Bike("blue", 89.99)
testTwo = Bike("purple", 25.0)

#AddOn --> Formatted Print

def __str__(self):
        return ("Color = {}, Price = {}".format(self.color, self.price))
 
 
 """ 2) Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing 
 a quantity of apples. The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method 
 called increase that increases the quantity by 1 each time it is invoked. You should also write a __str__ method for this class that 
 returns a string of the format: "A basket of [quantity goes here] [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket
 of 50 blue apples." (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)
 """
 class AppleBasket():
    
    def __init__(self, initColor, initQuantity):
        self.apple_color = initColor
        self.apple_quantity = initQuantity
    
    def increase(self):
        self.apple_quantity += 1
       
    def __str__(self): 
        return("A basket of {} {} apples.".format(self.apple_quantity, self.apple_color))

test1 = AppleBasket("red", 500)
print(test1)
test2 = AppleBasket("green", 20)
print(test2)
test1.increase()
print(test1)
 
