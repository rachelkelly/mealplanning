# A program to take in new recipes.
# Copyright Rachel Kelly 2014

import os # for pathy stuff?  not sure if necessary
from sys import exit


ingredients = []

def ingredient_input():
    ingredient = 0
    while ingredient != 'DONE':
        print "what is the ingredient?  no measurements yet, please.  type DONE"
        print "in all-caps if no more."
        ingredient = raw_input("> ")
        if ingredient == 'DONE':
            ingred_check()
        else:
            ingredients.append(ingredient)

def ingred_check():
    print ingredients
    print "is that all the ingredients? y or n?  if not, you can add to the list."
    total_ingredients = raw_input("> ")
    if total_ingredients == 'y':
        #here, write these ingredients to new_recipe file
        ingredient_quantity()
    elif total_ingredients == 'n':
        ingredient_input()
    else:
        print "y for yes and n for no."

copy_ingredients = ingredients
ingreds_with_quantity = []

def ingredient_quantity():
    while copy_ingredients != []:
        print "ok, for the ingredient " + copy_ingredients[-1] + ".  How much?"
        print "tsp = teaspoon.  tbsp = tablespoon.  c = cup.  fractions ok."
        quantity = raw_input("> ")
        print "ok, so " + quantity + " " + copy_ingredients[-1] + ".\n"
        ingreds_with_quantity.append(str(quantity + " " + copy_ingredients[-1]))
        new_file.write(copy_ingredients[-1])
        del copy_ingredients[-1]
        print "you've enumerated these: "
        print ingreds_with_quantity
        print "you have these ingreds left to enumerate:\n"
        print ingredients
        if copy_ingredients == []:
            #here, write ingreds_with_quantity\n to new_recipe file
            directions_input()

directions = []

def directions_input():
    # this is where the directions go.  hmm!
    print "made it to directions_input!"
    direction = 0
    while direction != 'DONE':
        print "what's the first/next instruction?  type DONE if, um, yknow."
        direction = raw_input("> ")
        if direction == 'DONE':
            print directions
            exit(0)
        else:
            directions.append(direction)
            new_file.write(direction) # this doesn't work, PRIORITY
            print "here's what you've got so far:\n"
            print directions

def beginning():
    print "what is the new recipe you wish to add?  no spaces."
    global new_recipe
    new_recipe = raw_input("> ")
    # now to check if that recipe already exists in file recipes/recipe_list
    # dummy list below, TO DELETE & coordinate with real file called recipe_list
    recipe_list = ["blt"]
    if new_recipe in recipe_list:
        print "that recipe is already in the file."
        exit(0)
    else:
        global new_filename
        new_filename = "recipes/" + new_recipe + ".txt"
        global new_file
        new_file = open(new_filename, 'a') #'a' for append rather than write
        # trying to make a new filename inside dir recipes based on given name
        recipe_list.append("\n" + new_recipe)
        ingredient_input()

beginning()
