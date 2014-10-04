# A program to take in new recipes.
# Copyright Rachel Kelly 2014

from sys import exit
import os.path       #os.path test

global new_recipe, new_file, new_filename

ingredients = []
ingreds_with_quantity = [] # based on ingreds but w/ quantity
directions = [] # this might need to be a dict instead?

def beginning():
    print "what is the new recipe you wish to add?  no spaces."
    global new_recipe
    new_recipe = raw_input("> ")
    list_file = open('recipes/recipe_list.txt', 'r') # lol single quotes
    if new_recipe in list_file:
        print "that recipe is already in the file."
        if os.path.isfile('recipes/' + new_recipe + '.txt'):
            print "plus we already got a recipe filename for it so that's gravy"
        # if the recipe is already in the file, also check that there's a .txt for it
            #if "recipes/" + new_recipe + ".txt" in "/recipes/" # want to put 'new_filename' in here instead
        list_file.close()
        exit(0)

    else:
        # adding recipe to recipe_list.txt
        list_file.close() #gotta close it first tho
        list_file = open("recipes/recipe_list.txt", 'a') # 'a' for append rather than
        list_file.write("\n" + new_recipe)               # write
        list_file.close()
        
        global new_filename
        new_filename = os.path.join('recipes/' + new_recipe + '.txt') # os.path test
                                                        
        global new_file
        new_file = open(new_filename, 'w')
        
        # trying to make a new filename inside dir recipes based on given name
        ingredient_input()

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

copy_ingredients = ingredients # created to iterate over & not mess with

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
            new_file.write(ingreds_with_quantity) # how to add newline???
            directions_input()


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


beginning()
