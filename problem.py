# python-constraint will do everything for me :-)
from constraint import *

# defining the variables
# colour
green = "green"
white = "white"
yellow = "yellow"
blue = "blue"
red = "red"

# nationality
sweden = "Sweden"
english = "English"
german = "German"
norwegian = "Norwegian"
dutch = "Dutch"

# cigarettes
blue_master = "Blue Master"
dunhill = "Dunhill"
blend = "Blend"
prince = "Prince"
pall_mall = "Pall Mall"

# drink
water = "water"
tea = "tea"
milk = "milk"
coffee = "coffee"
beer = "beer"

# animal
fish = "fish"
cat = "cat"
horse = "horse"
dog = "dog"
birds = "birds"

problem = Problem()

# defining the variables
colour = [green, white, yellow, blue, red]
nationality = [sweden, english, german, norwegian, dutch]
cigarettes = [blue_master, dunhill, blend, prince, pall_mall]
drink = [water, tea, milk, coffee, beer]
animal = [fish, cat, horse, dog, birds]

problem.addVariables(colour + nationality + cigarettes + drink + animal, [1, 2, 3, 4, 5])
problem.addConstraint(AllDifferentConstraint(), colour)
problem.addConstraint(AllDifferentConstraint(), nationality)
problem.addConstraint(AllDifferentConstraint(), cigarettes)
problem.addConstraint(AllDifferentConstraint(), drink)
problem.addConstraint(AllDifferentConstraint(), animal)

# constraints from wikipedia
# 1
problem.addConstraint(lambda eng, red: eng == red, [english, red])
# 2
problem.addConstraint(lambda swe, dog: swe == dog, (sweden, dog))
# 3
problem.addConstraint(lambda dut, tea: dut == tea, (dutch, tea))
# 4
problem.addConstraint(lambda gre, whi: whi-gre == 1, (green, white))
# 5
problem.addConstraint(lambda gre, cof: gre == cof, (green, coffee))
# 6
problem.addConstraint(lambda pal, bir: pal == bir, (pall_mall, birds))
# 7
problem.addConstraint(lambda yel, dun: yel == dun, (yellow, dunhill))
# 8
problem.addConstraint(InSetConstraint([3]), [milk])
# 9
problem.addConstraint(InSetConstraint([1]), [norwegian])
# 10
problem.addConstraint(lambda ble, cat: abs(ble-cat) == 1, (blend, cat))
# 11
problem.addConstraint(lambda hor, dun: abs(hor-dun) == 1, (horse, dunhill))
# 12
problem.addConstraint(lambda blu, bee: blu == bee, [blue_master, beer])
# 13
problem.addConstraint(lambda ger, pri: ger == pri, [german, prince])
# 14
problem.addConstraint(lambda nor, blu: abs(nor-blu) == 1, (norwegian, blue))
# 15
problem.addConstraint(lambda ble, wat: abs(ble-wat) == 1, (blend, water))
# who keeps the fish?

solution = problem.getSolutions()[0]

# get the right column
list = []
for i in range(5):
    for x in solution:
        if solution[x] == i:
            if fish in x:
                for j in range(5):
                    if j == i:
                        for x in solution:
                            if solution[x] == i:
                                if x in colour:
                                    fcolour = x
                                elif x in nationality:
                                    fnationality = x
                                elif x in cigarettes:
                                    fcigarette = x
                                elif x in drink:
                                    fdrink = x

# print the result
print(f"{fnationality} keeps fish, as well, he lives in a {fcolour} house number {j}, he smokes {fcigarette} - but that is not healthy! Our {fnationality} drinks {fdrink}.")
