import random 
import os



#current variables
current_level = 0
current_health = 100
current_location = "Town"
#current variables
xp = 0
money = 0

os.system('cls' if os.name == 'nt' else 'clear') 


    # base stats _______________________________________________________

    #static stats_________________________________________________________
class stats():
    def __init__(self,name,health,attack,defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense


wolf = stats("Wolf",10,1,0)
player = stats("player",100,1,1)
    #static stats_________________________________________________________


#dynamic stats____________________________________________________________
character = {
    player.name:{'name':player.name,'health':player.health,"attack":player.attack,"defense":player.defense},
    wolf.name:{'name':wolf.name,'health':wolf.health,"attack":wolf.attack,"defense":wolf.defense}
#dynamic stats____________________________________________________________
}
    # base stats _______________________________________________________

#combat section _______________________________________________________
class combat():
    # damage calculation
    def take_damage(attacker,defender,damage =0):
        if attacker["attack"] >= defender['defense']:
            accuracy = 1 + (attacker['attack']-defender['defense'])
            damage = (0.1*random.randint(1,accuracy*10))
        if attacker['attack'] <defender['defense']:
            accuracy =0.1 * random.randint(0,10)*(attacker['attack']/defender['defense'])
            damage = 1 + accuracy
        return damage
    # damage calculation



# combat instance _______________________________________________________
    def instance(player,enemy,reset):
        global current_health
        enemy['health'] = reset.health
        print(f"A wild {enemy['name']} has appeared")
        while enemy['health'] >=0 and current_health >=1:
            pannel()
            print(f"{enemy['name']}:{enemy['health']}")
            print("-"*100)

            print("a) to use melee attack")

            choice = input("select: ")
            if choice == 'a':
                enemy['health'] -= combat.take_damage(player,enemy)
            else: 
                pass
            current_health -=combat.take_damage(enemy,player)
        if enemy['health'] <=0:
            pannel()
            print(f"You have killed the {enemy['name']}")
            input("The wolf drops some bones, you pick them up.")
# combat instance _______________________________________________________
            
#combat section _______________________________________________________


#----------------------not a part of combat code
def pannel():
    '''
    This function displays the screen for each instance
    '''

    os.system('cls' if os.name == 'nt' else 'clear') 
    print("_"*100,'\n')
    print(f"health:{current_health}",'\t',f"xp: {xp}", '\t'*2,f"level: {current_level}","\t",f"money: ${money}","\t",f"Location: {current_location}")
    print("_"*100,'\n')

#----------------------not a part of combat code

while current_health > 0:
    combat.instance(character['player'],character['Wolf'],wolf)
if current_health <=0:
    print("You have died")
