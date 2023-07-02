import random


firstNames = ["David", "Michael", "Phillip", "Jane", "Asia", "Thomas", "Susie", "Grace", "Hannah", "John"]
lastNames = ["Smith", "McKenzie", "Brown", "Taylor", "Cooper", "Francis", "Walker", "Anderson", "Williams"]

firstName = input("What is your first name? ")
lastName = input("What is your last name? ")

newFirstName = firstNames[random.randint(0, (len(firstNames) - 1))]
newLastName = lastNames[random.randint(0, (len(lastNames) - 1))]

print("Well now your name is " + newFirstName + " " + newLastName)
