"""
Open VS code or Juypter Notebook

create an empty list named food = [ ] 

Add five different foods that you like but use the different methods to add items to list such as append and insert

print the list x 

Sort you list alphabetically x 

print the list again x 

for loop through the list and print each item out with a print statement that says you really like that food. x 

example output I really like to eat spaghetti. Please use the f - statement x 
"""

food = []

food.append("pizza")
food.insert(1, "apple")
food.insert(0, "bannana")
food.append("eggs")
food.append("tacos")


print(food)

food.sort()
print(food)

for items in food:
    print(f"I really like to eat {items}")