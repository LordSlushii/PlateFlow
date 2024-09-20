#last recommendation model god pls save me 
from tabulate import tabulate
import random

menu = {
    "Crispy Chicken Sandwich" : ["juicy", "crispy", "classic"],
    "Spicy Chicken Burrito" : ["spicy", "loaded", "tangy"],
    "Grilled Chicken Wrap" : ["fresh", "grilled", "light"],
    "Cheeseburger Deluxe" : ["cheesy", "deluxe", "toasted"],
    "Smoky BBQ Chicken Wings" : ["smoky", "juicy", "bold"],
    "Loaded Veggie Bowl" : ["loaded", "fresh", "herby"],
    "Crispy Nacho Fries" : ["crispy", "cheesy", "savory"],
    "Classic Chicken Club Sandwich" : ["classic", "crispy", "toasted"],
    "Spicy Chicken Tenders" : ["spicy", "tender", "crunchy"],
    "Deluxe Fish Sandwich" : ["deluxe", "crispy", "zesty"]
}

selectedItems = []
while True:
    item = input("Enter Item: ")
    if item == "0":
        break
    else:
        selectedItems.append(item)
    


selectedItemKeys = [] 
FselectedItemKeys = []
for i in selectedItems:
    selectedItemKeys += menu[i]

for i in selectedItemKeys:
    if i in FselectedItemKeys:
        pass
    else:
        FselectedItemKeys.append(i)
    

points = []
for i in FselectedItemKeys:
    points.append([i, selectedItemKeys.count(i)])
sorted_points = sorted(points, key=lambda x: x[1], reverse = True)


recommendations = ["Pepsi", "Fries"]
reclis = []
for i in menu:
    if sorted_points[0][0] in menu[i]:
        if i in selectedItems:
            pass
        else:
            reclis.append(i)

print(random.choice(reclis))


