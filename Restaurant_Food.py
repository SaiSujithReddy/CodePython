'''
Career cup Yelp
"American", "[Burger, French fries, Potato Chips]"
"Italian", "[Pizza, Bread Sticks, Potato Chips]"

'''


def list_rest_where_this_type_of_food_is_available(food):


    dict_rest_food = {
        "American": ["Burger", "French fries", "Potato Chips"],
        "Italian": ["Pizza", "Bread Sticks", "Potato Chips"]
    }

    for x in dict_rest_food:
        for y in dict_rest_food[x]:
            if y == food:
                print(x,end=" ")


list_rest_where_this_type_of_food_is_available("Potato Chips")