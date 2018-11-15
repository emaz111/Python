"""

Sweet shop

This program allows the user to enter prices of five sweets using a for loop and
then stored in a tuple named 'Price'.

Using the Prices stored in the tuple, the program can output the total price of
all the sweets, the average, the highest costing sweet and finally the lowest
costing sweet

"""
"""
__Author__ = Emaz Khan
__Email__ = U1859269@unimail.hud.ac.uk
__Date__ = Thursday 27th October 2018
"""

Price = []

for i in range(5):
    Item_Cost = input("Enter the price of the sweet: ")
    if Item_Cost.endswith("p"):
        Item_Cost = Item_Cost[:-1]
        Price.append(int(Item_Cost))
    else:
        Price.append(int(Item_Cost))

print("Total Price: " + str(sum(Price)) + " p")
print("Average Price: " + str(sum(Price) / len(Price)) + " p")
print("Highest Price: " + str(max(Price)) + " p")
print("Lowest Price: " + str(min(Price)) + " p")
