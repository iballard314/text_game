import os
import random

island_name = "island"

#current variables
current_level = 1
current_health = 100
current_location = "Town"
#current variables

game_loop = True



money = 0
xp = 0


location = {
    "Town":{"a":"Jungle","b":"Shop","c":"Dock"},
    "Shop":{"a":"Town"},
    "Jungle":{"a":"Town"},
    "Dock":{"a":"Town","b":"Shop","c":"Travel"},

}
# item storage _____________________________________________________________________________________________________________


    # base stats _______________________________________________________
class stats():
    def __init__(self,name,health,attack,defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense


wolf = stats("Wolf",10,1,0)
player = stats("player",100,1,1)

character = {
    player.name:{'name':player.name,'health':player.health,},
    wolf.name:{'name':wolf.name,'health':wolf.health,}
}
    # base stats _______________________________________________________



def function():
    pass

class item():
    def __init__(self,name,sell,buy,rare,effect,description):
        self.name



class backpack():

    storage = {
        "health potion":{"name":"health potion","sell":100,"buy":200,"quantity":3,"effect":function,'description':"a potion that heals 10",'combat':True},
        "wolf bone":{"name":"wolf bone","sell":450,"buy":250,"quantity":0,"effect":function,'description':"bones of the wolf terroizing the city",'combat':False,}
               }

    def add_to_backpack(item_name,sell,buy,quantity,function,description):
        backpack.storage[item_name]["name"] = item_name
        backpack.storage[item_name]['sell'] = sell
        backpack.storage[item_name]['buy'] = buy
        backpack.storage[item_name]['quantity'] = quantity
        backpack.storage[item_name]['effect'] = function
        backpack.storage[item_name]['description'] = description

    def display(storage):
        for key in storage:
            if storage[key]['quantity'] >=0:
                print('\n',f"|item: {storage[key]['name']}| sells for {storage[key]['sell']} | quantity: {storage[key]['quantity']}| description: {storage[key]['description']}",'\n')


    def combat_access(storage):
        for key in storage:
            if storage[key]['combat'] ==True:
                print(f"item: {storage[key]['name']}")

# item storage _____________________________________________________________________________________________________________


def pannel():
    '''
    This function displays the screen for each instance
    '''

    os.system('cls' if os.name == 'nt' else 'clear') 
    print("_"*100,'\n')
    print(f"health:{current_health}",'\t',f"xp: {xp}", '\t'*2,f"level: {current_level}","\t",f"money: ${money}","\t",f"Location: {current_location}")
    print("_"*100,'\n')

def message(*text):
    for i in text:
        print(i)
    print("-"*100, '\n')


# functions for events and dialogue for locations ____________________________________________________________________________________
def town():
    message = ["Welcome to the town of varador","You notice there arent many people around."]

    return message

def shop():
    message = ["Welcome to the shop of varador","What would you like to buy or sell?."]

    return message

def Jungle():
    message = ["You leave the city, all around you is dense jungle","You walk a bout couple hundred feet.", "When suddenly you hear a noise, and get the feeling you are bing watched."]

    return message


# functions for events and dialogue for locations ____________________________________________________________________________________




#travel function_____________________________________________________________________________________________________________________
def travel(current):
    '''
    This functions goal is to give traveling options for each location
    and allow the player to chose where they would like to go.
    
    '''
    for key,value in location[current].items():
        print(f"{key}:{value}")

    choice = input("Select an option: ")

    try:
        for key in location[current]:
            if choice == key:
                current =location[current][choice]
                return current
            else:
                pass
    except KeyError:
        pannel()
        print("You choice was invalid.")
        travel(current)
        
    return current
#travel function______________________________________________________________________________________________________________________

# game loop___________________________________________________________________________________________________________________________


while game_loop == True:
    if current_health >=1:
        pannel()
        if current_location == 'Town':
            text = town()
        if current_location == 'Shop':
            text = shop()
        if current_location == 'Jungle':
            text = Jungle()
        message(*text)
        input("Press enter to continue")
        current_location = travel(current_location)
    if current_health <= 0:
        print("You have died!.")
        break

# game loop___________________________________________________________________________________________________________________________
