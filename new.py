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
        # new_file.write(ingredients)
        ingredient_quantity()
    elif total_ingredients == 'n':
        ingredient_input()
    else:
        print "y for yes and n for no."
        ingred_check()

copy_ingredients = ingredients
ingreds_with_quantity = []

def ingredient_quantity():
    while copy_ingredients != []:
        print "ok, for the ingredient " + copy_ingredients[-1] + ".  How much?"
        print "tsp = teaspoon.  tbsp = tablespoon.  c = cup.  fractions ok."
        quantity = raw_input("> ")
        print "ok, so " + quantity + " " + copy_ingredients[-1] + ".\n"
        ingreds_with_quantity.append(str(quantity + " " + copy_ingredients[-1]))
        del copy_ingredients[-1]
        print "you've enumerated these: "
        print ingreds_with_quantity
        print "you have these ingreds left to enumerate:\n"
        print ingredients
        if copy_ingredients == []:
            new_file.write(ingreds_with_quantity)
            directions_input()

directions = []

def directions_input():
    print "made it to directions_input!"
    direction = 0
    while direction != 'DONE':
        print "what's the first/next instruction?  type DONE if, um, yknow."
        direction = raw_input("> \n")
        if direction == 'DONE':
            print directions
            exit(0)
        else:
            directions.append(direction)
            new_file.write(direction)
            print "here's what you've got so far:\n"
            print directions

def beginning():
    print "what is the new recipe you wish to add?  no spaces."
    global new_recipe
    new_recipe = raw_input("> ")
    list_file = open("recipes/recipe_list.txt", 'a') # don't want to overwrite athg!
    if new_recipe in list_file: # "IOError: File not open for reading" uh oh
        print "that recipe is already in the file."
        list_file.close()
        exit(0)
    else:
        global new_filename
        new_filename = "recipes/" + new_recipe + ".txt"
        global new_file
        new_file = open(new_filename, 'w')
        
        list_file.write(new_recipe)

        # trying to make a new filename inside dir recipes based on given name
        recipe_list.append("\n" + new_recipe)
        ingredient_input()

beginning()
