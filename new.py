# A program to take in new recipes.
# Copyright Rachel Kelly 2014

import sys
import os.path
from AppKit import NSBeep

global new_recipe, new_file, new_filename

ingredients = []
ingreds_with_quantity = [] # based on ingreds but w/ quantity, not sure if necessary
directions = [] # this might need to be a dict instead?

def beginning():
    print "what is the new recipe?  if the recipe is already in recipe_list/, then"
    print "we won't write over it."
    global new_recipe
    new_recipe = raw_input("> ")
    
    f = open('recipes/recipe_list.txt', 'r')
    for line in f.readlines():
        if new_recipe in line:
            NSBeep() # this might not stay in the same function
            print "BZZZZT.  You already put that recipe in the recipe_list dir."
            if os.path.isfile('recipes/' + new_recipe + '.txt'):
        	    print "plus we already got a recipe filename for it so that's gravy."
        	    f.close()
        	    sys.exit()
        else:
            print line
            print "checking line .."
    print "ok.  looks like we've got a new recipe after all!"
    f.close()
    recipe_adder()
        

def recipe_adder():
    # adding recipe to recipe_list.txt
    list_file = open("recipes/recipe_list.txt", 'a')
    new_rec_with_newline = '\n' + new_recipe
    list_file.write(new_rec_with_newline) # think it's working!
    list_file.close()

    global new_filename
    new_filename = os.path.join('recipes/' + new_recipe + '.txt')                                                        
    global new_file
    new_file = open(new_filename, 'w')
    
    ingredient_input()


def ingredient_input():
    ingredient = 0
    global new_file
    new_file = open(new_filename, 'w')
    while ingredient != 'DONE':
        print "what is the ingredient?  no measurements yet, please.  type DONE"
        print "in all-caps if no more."
        ingredient = raw_input("> ")
        if ingredient == 'DONE':
            new_file.close()
            ingred_check()
        else:
            ingredients.append(ingredient)            
            new_file.write(ingredient)
            new_file.write('\n')
            
              
copy_ingredients = ingredients # created to iterate over & not mess with

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
            global new_file
            new_file = open(new_filename, 'w')
            new_file.write(ingreds_with_quantity)
            new_file.close()
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
