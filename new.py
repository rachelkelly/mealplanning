# A program to take in new recipes.
# Copyright Rachel Kelly 2014

import os
from sys import exit
    
ingredients = []


def ingredient_input():
    print "what is the first ingredient?  no measurements yet, please"
    first_ingredient = raw_input("> ")
    ingredients.append(first_ingredient)
    print ingredients
    more_ingredients = True
    while more_ingredients == True:
        print "what's the next ingredient?"
        next_ingredient = raw_input("> ")
        ingredients.append(next_ingredient)
        print "are there more ingredients?  type True or False."
        more_ingredients = raw_input("> ")
    else:
        ingred_check()


def ingred_check():
    print ingredients
    print "is that all the ingredients? y or n?  if not, we're"
    print "just going to erase it & start over at this point."
    # will not always be this way - at some point I'll allow editing of ingreds.
    total_ingredients = raw_input("> ")
    if total_ingredients == 'y':
        directions_input()
    elif total_ingredients == 'n':
        ingredient_input()
        # this'll send you back, with current ingredient list deleted.
    else:
        print "y for yes and n for no."



def directions_input():
    for i in ingredients_list:
        print "how much of " + ingredients_list[i] + "?"
        quantity = raw_input("> ")

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
