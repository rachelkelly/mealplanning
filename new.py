# A program to take in new recipes.
# Copyright Rachel Kelly 2014

import os
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
        ingredient_quantity()
    elif total_ingredients == 'n':
        ingredient_input()
    else:
        print "y for yes and n for no."

copy_ingredients = ingredients

def ingredient_quantity():
    while copy_ingredients != []:
        print "ok, for the ingredient " + copy_ingredients[-1] + ".  How much?"
        print "tsp = teaspoon.  tbsp = tablespoon.  c = cup.  fractions ok."
        quantity = raw_input("> ")
        print "ok, so " + quantity + " of " + copy_ingredients[-1] + ".  Right?"
        print "if not," # then we'll have some conditional repeat thingie later.
        list.pop(copy_ingredients)
        print "there are " + copy_ingredients.count() + " left." #line not necessary

def beginning():
    print "what is the new recipe you wish to add?  no spaces."
    new_recipe = raw_input("> ")
    # now to check if that recipe already exists in a TBD list
    # dummy list below, TO DELETE & coordinate with real file called recipe_list
    recipe_list = ["blt"]
    if new_recipe in recipe_list:
        print "that recipe is already in the file."
        exit(0)
    else:
        open("recipes/" + new_recipe + ".txt", 'a')
        # trying to make a new filename inside dir recipes based on given name
        recipe_list.append("\n" + new_recipe)
        ingredient_input()

beginning()
