from random import randint
import gaming_tools

def restart_game() :
    """resets the game and starts another one
    
    """
    gaming_tools.reset_game()
    print('You have restarted the game, have fun with another one')



def new_character(character, variety) :
    """Create a character with a name and a variety
 
     Parameters
    ----------
    character : name of the character (str)
    variety : type of the character (str)
   
    """

    ##checks if the character exists or not
    if gaming_tools.character_exists(character) == True :
        print('You already created a character with that name.')
    else :
        if variety == 'dwarf' or variety =='necromancer' or variety =='wizard' or variety =='healer' or variety =='elf' :
            if variety == 'dwarf' :
                strength = randint(10, 50) 
                life = randint(10, 50)
                reach = 'short'
            elif variety == 'necromancer' or variety == 'wizard' or variety =='healer' :
                strength = randint(5, 15)
                life = randint(5, 15)
                if variety == 'wizard' :
                    reach = 'long'
                elif variety == 'necromancer' or variety == 'healer' :
                    reach = 'short'
            elif variety == 'elf' :
                strength = randint(15, 25)
                life = randint(15, 25)
                reach = 'long'
            ##+50 money team
            gaming_tools.set_team_money(gaming_tools.get_team_money()+50)
            print('Your team has got %i money' % (gaming_tools.get_team_money()))
            print('%s the %s has been created, he has %i strength and %i life. He has a %s reach.' % (character, variety, strength, life, reach))
            gaming_tools.add_new_character(character, variety, reach, strength, life)
        else :
            print('That variety doesn\'t exist')


 
def attack_creature(character, creature):
    """attack a select creature with a select character and vice versa  
 
    Parameters
    ----------
    character : name of the character (str)
    creature : name of the creature (str)
    """
    
    if gaming_tools.character_exists(character) == False or gaming_tools.get_character_life(character) <= 0 :
        print('You cannot attack if your character doesn\'t exist or if he\'s dead')
    else : 
        ##the character attacks the creature first 
        ##checks the reach
        if gaming_tools.get_creature_reach(creature) == 'long' and gaming_tools.get_character_reach(character) == 'short' :
            print('Your character cannot attack a creature with a long reach')
        else :
            print('%s attacks %s, he deals %i damage' % (character, creature, gaming_tools.get_character_strength(character)))
            
            if gaming_tools.get_creature_life(creature) > gaming_tools.get_character_strength(character) :
                gaming_tools.set_creature_life(creature, gaming_tools.get_creature_life(creature)-gaming_tools.get_character_strength(character))
                print('The creature has now %i hp' % (gaming_tools.get_creature_life(creature)))
                ##the creature fights back if it's still alive
                ##checks its reach
                if gaming_tools.get_character_reach(character) == 'long' and gaming_tools.get_creature_reach(creature) == 'short' :
                    print('The creature cannot fight back because of its short reach')
                else :
                    print('%s fights back and deals %i damage to %s' % (creature, gaming_tools.get_creature_strength(creature), character))
                    gaming_tools.set_character_life(character, gaming_tools.get_character_life(character)-gaming_tools.get_creature_strength(creature))
                    if gaming_tools.get_character_life(character) <= 0 :
                        print('Your character is dead')
                    else :
                        print('Your character is fine')
            else :
                print('The creature has been defeated and doesn\'t fight back')
                gaming_tools.remove_creature(creature)
                gaming_tools.set_nb_defeated(gaming_tools.get_nb_defeated()+1)
                ##gain gold    
                gold_gain = 40 +10*(gaming_tools.get_nb_defeated())
                gaming_tools.set_team_money(gaming_tools.get_team_money()+gold_gain)
                print('Your team has now %i gold coins' % (gaming_tools.get_team_money()))


 
def evolve(character) : 
    """Evolve a character with the agreement of the others players    
 
    ----------
    Parameters
    character : name of the character (str)
   
    """
    #checks if the character exists
    if gaming_tools.character_exists(character) == False or gaming_tools.get_character_life(character) <= 0 :
        print('The character doesn\'t exist or if you\'re dead')

    else : 
        #checks if enough money
        if gaming_tools.get_team_money() < 4 :
            print('You don\'t have enough money to evolve that character')

        else : 
            #upgrade life
            if randint(0,1) == 1 :
                gaming_tools.set_character_life(character, gaming_tools.get_character_life(character)+2)
                print('Your life has been improved, your character has now %i hp' % (gaming_tools.get_character_life(character)))
            else :
                print('Your character life hasn\'t been improved')
            #upgrade strength
            if randint(0,3) == 3 :
                gaming_tools.set_character_strength(character, gaming_tools.get_character_strength(character)+4)
                print('Your strength has been improved, you have now %i strength' % (gaming_tools.get_character_strength(character)))
            else :
                print('Your strength hasn\'t been improved')
            #4 gold coins cost
            gaming_tools.set_team_money(gaming_tools.get_team_money()-4)
            print('Your team has lost 4 gold coins')



def heal(character, target) :
    """heals a target if the selected character is a heal
    
    Parameters : 
    ------------
    character : name of the character (str)
    target : name of the character who gets healed (str)
    
    """
    #checks if the character exists
    if gaming_tools.character_exists(character) == False or gaming_tools.get_character_life(character) <= 0:
        print('Your character does not exist')
    #checks if character is healer
    elif gaming_tools.get_character_variety(character) != 'healer' :
        print('Your character cannot cast that spell')
    #checks if the target exists
    elif gaming_tools.character_exists(target) == False :
        print('The target doesn\'t exist')
    #casts the spell
    else :
        print('%s casts a healing spell on %s' % (character, target))
        gaming_tools.set_character_life(target, gaming_tools.get_character_life(target)+10)
        print('%s has now %i hp' % (target, gaming_tools.get_character_life(target)))



def revive(character, target) :
    """revives a dead character for 75 gold coins and gives him 10HP

    Parameters :
    ----------
    character : name of the character who casts the reviving spell (str)
    target : name of the ally character who gets revived (str)
    """
    #checks if the character exists or if he's dead
    if gaming_tools.get_character_life(target) != 0 or gaming_tools.character_exists == False :
        print('You cannot revive somebody still alive or somebody who doesn\'t exist')
    #checks if character is necromancer
    elif gaming_tools.get_character_variety(character) != 'necromancer' or gaming_tools.get_character_life(character) <= 0:
        print('You cannot revive someone if you\'re not a necromancer or if you\'re dead')
    #casts the reviving spell
    else : 
        gaming_tools.set_character_life(target, life=10)
        gaming_tools.set_team_money(gaming_tools.get_team_money()-75)
        print('%s has been revived and your team has lost 75 gold coins. You still have  %i gold coins' % (target, gaming_tools.get_team_money()))



def wizard_spell(character, creature) :
    """divide the creature's hp by two for 20 gold coins
    
    Parameters :
    ------------
    character : name of the character who casts the spell(str)
    
    """
    #checks if there's a creature
    if gaming_tools.is_there_a_creature() == False :
        print('There isn\'t any creature to cast a spell on')
    #checks if wizard
    elif gaming_tools.get_character_variety(character) != 'wizard' or gaming_tools.get_character_life(character) <= 0 :
        print('You cannot cast that spell if you\'re not a wizard or if you\'re dead')
    #casts the spell
    else :
        if gaming_tools.get_team_money() >= 20 :
            print('You cast a spell on the creature, it divides its hp by 2')
            gaming_tools.set_creature_life(creature, gaming_tools.get_creature_life(creature)/2)
            print('%s has now %i hp' % (creature, gaming_tools.get_creature_life(creature)))
            ##set the team's money
            gaming_tools.set_team_money(gaming_tools.get_team_money()-20)
            print('Your team has now %i gold coins' % (gaming_tools.get_team_money()))
        else : 
            print('You don\'t have enough money to cast that spell')


def new_creature ():
    """"Create a creature with a random name and a random strength/life/reach""

   ---------------------------------------------------------------------------
   """
    #checks if already a creature
    if gaming_tools.is_there_a_creature() == False :
       #set a name for the creature
        creature = gaming_tools.get_random_creature_name()
       # set the creature strength and life
        strength = randint(1, 10) * (1+gaming_tools.get_nb_defeated())
        life = randint(1, 10) * (1+gaming_tools.get_nb_defeated())
       #set the creature reach
        reach = randint(1,2)
        if (reach == 1):
            reach = 'short'
        else :
            reach = 'long'
        gaming_tools.add_creature(creature, reach, strength, life)
        print('A creature has spawned, it is named %s, it has %i strength and %i life and it has a %s reach' % (creature, gaming_tools.get_creature_strength(creature), gaming_tools.get_creature_life(creature), gaming_tools.get_creature_reach(creature))) 
    else : 
        print('There\'s already a creature')


restart_game()




## pas oublier de bien renommer le fichier rendu et le rapport comme demandé sur la feuille


