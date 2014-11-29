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
        	    # give opportunity to edit?  shouldn't be too hard... hmmmmmm
        	    f.close()
        	    sys.exit()
        else:
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
    copy_ingredients = ingredients # created to iterate over & not mess with
                               # they call me the DRY violator, the DRYolator
                               # the WETsmith
                               # write everything thrice
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
        new_file.write(str(ingreds_with_quantity)) #expected a character buffer obj
        new_file.close()                           #put str() around it fixed it...
    	directions_input()                         #that seems really dumb


def directions_input():
    '''
    directions_input: takes one step of instruction at a time, then takes the indexing
    integer, stringifies it, and tacks it onto the front via the redefinition of the 
    `direction` variable.  then, it prints it out which is debugging behavior.  then 
    index += 1 & starts over back again as direction still does not equal 'DONE'.  
    
    I want to add a \n at the end of each one so it prints out recipe-style.
    
    I think I want to simplify this whole fn.
    
    '''
    directions = []
    print "made it to directions_input!"
    direction = 0 # wait why is this here
    i = 1 # indexing & numeration
    while direction != 'DONE':
        print "what's the first/next instruction?  type DONE if, um, yknow."
        direction = raw_input("> ")
        
        if direction == 'DONE':
			print directions
			print "ok now we'll write this to file."
			new_file = open(new_filename, 'a+')
			new_file.write(str(directions))
			new_file.write('\n')
			finish_it_up()
        
        else:
            print "ok, the latest direction is ", direction # for debug
            j = str(i) # why can't I just have below line be 'dir = str(i + ". " + dir)'?
            direction = j + ". " + direction + "\n"
            #directions.append(direction) # maybe I DON'T want this in a list.
            new_file = open(new_filename, 'a+')
            new_file.write(direction)
            
            #print "here's what you've got so far:\n" # commenting out bc experimenting w
            #print directions                         # not having a directions list.
            i += 1
    print "ok now we'll write this to file."
    #new_file = open(new_filename, 'a+')
    #new_file.write(str(directions))
    finish_it_up()

# def feeds_how_many():

def finish_it_up():
    # print file name (desluggified filename?) and print out complete recipe
    print str(new_filename)
    print directions

beginning()