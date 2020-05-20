# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:58:22 2020

@author: Hi
"""

# Chef's Ingrredients
# 1) The chef receives 1 ingredient per day. It does not repeat
# 2) Ingredient belongs to Fiber, Fat & Carb
# 3) Every ingredient has a unique ingredient id - Ingredient id starts with the category name like 
# FIBERBrocoli, FATCheese, CARBRice

# Chef's Dishes
# 1) All of the chef's dishes will have constant number of ingredients - 1st input
# 2) Full ingredient will be used - no partial quantity
# 3) Chef's dishes will have at least 60% of the ingredients from a single category

#Chef's Cooking style
# 1) Chef chooses the oldest ingredients in the order of the arrival
# 2) Cannot use the same ingredient again
# 3) Can make a maximum of 1 dish per day
# 4) If the chef doesn't have enough ingredient, he does not make the dish

# input array of ingredients, we have to say when the chef cooks and when he does not

'''1) Loop through the number of days
2) Based on the number of ingredients input, start the slice of the ingredients from that day, 
mark the previous ones as "-"
3) Calculate the ceil of 60% based on the number of ingredients used
4) Split the string of ingredients to form the list
5) Slice the list based on the number of ingredients, as like ingredientList[0:<no_of_ing>]
6) Loop through the list, slice each of the string to count the number of Fat, Fiber and Carb, 
create a dictionary to add the count as value
7) Check if there is any value which is equal to ceil of 60%, fetch those values from the slice of list
8) Pop that value from the list
9) Slice the list based on the remaining values and for the next loop, again make the count of the 
ingredients in the dict
10) Check for the value equal to 60% and fetch the value for the next day. If there is no value =, 
make it "-" '''

import math

string_val = ""
number_of_days = 12
number_of_ing = 4
ing_str = "FATOil FIBERSpinach CARBRice FATCheese FIBERBeans FATEgg FIBERBrocolli CARBPotato CARBCorn \
FATOlive FIBERCarrot CARBBeetroot"
ing_list = ing_str.split(" ")
ing_count = {"FAT":0, "FIBER":0, "CARB":0}

items_in_a_category = math.ceil(0.6 * number_of_ing)

def remove_ing_val(list_of_used_ing):
    for index_val, used_ing_val in enumerate(list_of_used_ing):
        #print("used_ing_val", used_ing_val)
        if index_val != len(list_of_used_ing)-1:
            global string_val
            string_val += used_ing_val+";"
        else:
            string_val += used_ing_val

def check_percentage_matching_ing(ing_list_slice):
    match_ing_list = []
    order_ing_list = [None] * len(ing_list_slice)
    global ing_count
    #print("ing_count in check_percentage", ing_count)
    for selected_ing, count in ing_count.items():
        #print(selected_ing, count)
        #print(items_in_a_category)
        if count >= items_in_a_category:
            for ing_v in ing_list_slice:
                if selected_ing in ing_v:
                    match_ing_list.append(ing_v)
                    #print(match_ing_list)
    
    ing_count = {"FAT":0, "FIBER": 0, "CARB": 0}
    
    #print(match_ing_list)
    if len(match_ing_list) == 0:
        global string_val
        string_val += "-"
    else:
        #order_ing_list_not_null = list(filter(lambda k: k != None, order_ing_list))
        for val in match_ing_list:
            #print("val", val)
            match_val_ind = ing_list_slice.index(val)
            #print("match_val_ind", match_val_ind)
            #print("length_order_ing_list", len(order_ing_list))
            order_ing_list[match_val_ind] = val
        for rem_ing in ing_list_slice:
            filter_not_null = list(filter(lambda ing_val: ing_val != None, order_ing_list))
            if rem_ing not in match_ing_list and len(filter_not_null) != number_of_ing:
                rem_ing_index = ing_list_slice.index(rem_ing)
                order_ing_list[rem_ing_index] = rem_ing
        filter_not_null = list(filter(lambda ing_val: ing_val != None, order_ing_list))
        #print("filter_not_null", filter_not_null)
        remove_ing_val(filter_not_null)

def count_ing(ing_list_slice):
    global ing_count
    for ing_val in ing_list_slice:
        slice_ing_val = ing_val[0:2]
        if slice_ing_val == "FA":
            ing_count["FAT"] += 1
        elif slice_ing_val == "FI":
            ing_count["FIBER"] += 1
        elif slice_ing_val == "CA":
            ing_count["CARB"] += 1
    #print("ing_count", ing_count)
    check_percentage_matching_ing(ing_list_slice)
    #print(string_val)

def loop_days(ing_list):
    for day in range(1, number_of_days+1):
        if day < number_of_ing:
            #print("day", day)
            global string_val
            string_val += "-"
        else:
            #print("day", day)
            #print("ing_list", ing_list)
            ing_list_slice = ing_list[0:day]
            #print("ing_list_slice", ing_list_slice)
            modified_ing_list = list(filter(lambda v: v not in string_val, ing_list_slice))
            #modified_ing_list = [ing_val if ing_val not in string_val for ing_val in ing_list_slice]
            count_ing(modified_ing_list)
    print(string_val)
loop_days(ing_list)
