from timeit import default_timer as timer
import random

################################################################# Beginning ###############################################################

def startscreen():
    startorend = input(f'''[={'-'*85}=]
    
{"Tower of Babel": ^85}

{"[1] < S T A R T >": ^85}                                
{"[2]  < E N D >": ^85}                                  
                                 
>>>Enter: ''')
    while startorend!="1" and startorend!="2":
        print("Invalid choice...Please Try Again.")
        startorend = input(f'''[={'-'*85}=]
{"#name/text graphic": ^85}
{"[1] < S T A R T >": ^85}                                
{"[2]  < E N D >": ^85}                                  
                                 
>>>Enter: ''')
    return(startorend)

def choosediff():
    difficulty = input(f'''
[={'-'*85}=]
Select difficulty/mode: [1]Easy   [2]Moderate   [3]Hard   [4]Hardcore   [5]Speedrun

>>>Enter: ''')
    while difficulty not in("1","2","3","4","5"):
        print("Invalid choice...Please Try Again.")
        difficulty = input(f'''
[={'-'*85}=]
Select difficulty/mode: [1]Easy   [2]Moderate   [3]Hard   [4]Hardcore   [5]Speedrun

>>>Enter: ''')
    return(difficulty)

def choosecharacter():
    choice="No"
    while choice!='Yes' or choice!='yes':
        charcter = input(f'''
[={'-'*95}=]
Select Your Hero: [1] Warrior    ( Low damage, High health      )    Ability: Berserker's Roar
                  [2] Ninja      ( High damage, Low health      )    Ability: Vital Strike
                  [3] Druid      ( Medium damage, Medium health )    Ability: Vine Grasp
                  [4] Mage       ( High damage, Low health      )    Ability: Fireball

>>>Enter: ''')
        if charcter=="1":
            print("Trained under the mighty supersoldier Lieutenant Sterling, blood-thirsty warrior Kane is out to avenge the death of his father, who was killed by one of the members of the Supreme Six. Armed with lethal explosives, Kane is ruthless, and will not let anything stand in his way, not even death itself.\nBerserker's Roar: Temporarily increases health and damage.")
            choice = input('Do you want to choose this hero? (Yes/No): ')
            if choice == 'Yes' or choice == 'yes': return({'damage': 3, 'health': 33, 'ability': 'BerserkersRoar', 'name': 'Warrior' })
        elif charcter=="2":
            print("Born in the land of the Hidden Village, Asahi was destined to be a skilled assassin ever since he was born. Known as the human embodiment of\nstealth, Asahi is able to execute targets with four-edged shurikens in a blink of an eye. With an outstanding kill count of 21,583, Asahi is\ntasked to eliminate the leader of the Supreme Six.\nVital Strike: Targets the enemy's vitals, dealing double damage.")
            choice = input('Do you want to choose this hero? (Yes/No): ')
            if choice == 'Yes' or choice == 'yes': return({'damage': 5, 'health': 22, 'ability': 'VitalStrike', 'name': 'Ninja'})
        elif charcter=="3":
            print('A firm worshipper of the spiritual mythology Shaddai, Orion had been religiously studying the mystical arts of warping earth-based matter for\nover 500 years. Nominated as the next Great Protector, Orion fires wooden axes at very high speeds towards his enemies. Inclined to showcase\nthe true potential of Shadai, Orion has set his eyes on the Supreme Six.\nVine Grasp: Roots the enemy, immobilizing them for one turn.')
            choice = input('Do you want to choose this hero? (Yes/No): ')
            if choice == 'Yes' or choice == 'yes': return({'damage': 4, 'health': 26, 'ability': 'VineGrasp', 'name': 'Druid'})
        elif charcter=="4":
            print('Granted with the ability to element-bend on command, Light was first exposed to wizardry behind the supervision of the nigh omnipotent\nalchemist, Endora. Light carries a magic wand that shoots out powerful beams of energy. Having now expanded his array of spells, the sky provesto be the limit for the young sorcerer Light.\nFireball: Launches a ball of flames, deal damage immediately and in next turn.')
            choice = input('Do you want to choose this hero? (Yes/No): ')
            if choice == 'Yes' or choice == 'yes': return({'damage': 5, 'health': 24, 'ability': 'Fireball', 'name': 'Mage'})
        else:
            print("Invalid choice...Please Try Again.")
            choice="No"
        if choice not in("Yes","No","yes","no"):
            print("Invalid choice...Please Try Again.")

def datadifficulty(difficulty,chardata):
    if difficulty == '1': 
        chardata['damage'] += 1
        chardata['health'] += 2
    if difficulty == '3':
        chardata['health'] -= 1
    if difficulty == '4':
        chardata['damage'] -= 1
        chardata['health'] -= 1
    return(chardata)

################################################################# Contents ###############################################################

def generate_map():
    while True:
        res_map = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                   ['X','·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', 'X'],
                   ['X','·', '·', '·', '·', '·', '·', '·', 'X', '·', '·', '·', '·', '·', 'X'],
                   ['X','·', '·', 'X', '·', '·', '·', '·', '·', '·', 'X', 'X', 'X', '·', 'X'],
                   ['X','·', '·', '·', '·', '·', 'X', '·', '·', '·', '·', '·', '·', '·', 'X'],
                   ['X','P', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', 'X'],
                   ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        used_pos = [(5, 1), (4, 1), (5, 2), (4, 2)]
        o = (random.randint(1, 5), random.randint(1, 13))
        while o in used_pos or res_map[o[0]][o[1]] == 'X':
            o = (random.randint(1, 5), random.randint(1, 13))
        res_map[o[0]][o[1]] = 'O'
        around_pos = [(o[0] + 1, o[1]), (o[0] - 1, o[1]), (o[0], o[1] + 1), (o[0], o[1] - 1)]
        used_pos += [o] + around_pos
        random.shuffle(around_pos)
        c = None
        while c is None:
            row = random.randint(1, 5)
            col = random.randint(1, 13)
            if (row, col) not in used_pos:
                c = (row, col)
                res_map[row][col] = 'C'
        has_m = False
        for pos in around_pos:
            x, y = pos
            if not has_m and res_map[x][y] == '·':
                res_map[x][y] = 'M'
                has_m = True
            elif res_map[x][y] == '·':
                res_map[x][y] = 'X'
        for i in res_map:
            print(''.join(i))
        break
    return res_map

def checkmove(move,mapdata,playerpos1,playerpos2):
    if move not in("W","A","S","D","w","a","s","d"):
        print("Invalid move, please try again.")
        return False
    if move=="W" or move=="w":
        if mapdata[playerpos1-1][playerpos2]=="X":
            print("Invalid move, please try again.")
            return False
        else:
            playerpos1=playerpos1-1
    if move=="A" or move=="a":
        if mapdata[playerpos1][playerpos2-1]=="X":
            print("Invalid move, please try again.")
            return False
        else:
            playerpos2=playerpos2-1
    if move=="S" or move=="s":
        if mapdata[playerpos1+1][playerpos2]=="X":
            print("Invalid move, please try again.")
            return False
        else:
            playerpos1=playerpos1+1
    if move=="D" or move=="d":
        if mapdata[playerpos1][playerpos2+1]=="X":
            print("Invalid move, please try again.")
            return False
        else:
            playerpos2=playerpos2+1
    return playerpos1,playerpos2

################################################################ Fighting ##################################################################

def fightscreen(chardata,mondata,name):
    print(f'''[={name:-^80}=]
                                 
{"Your Health: "+str(chardata["health"])+"                    "+mondata["name"]+" Health: "+str(mondata["health"]): ^85}
 ''')

def fightmonster(monsters,mondatas,chardata):
    choice = random.choice(monsters)
    mondata = mondatas[choice]
    if mondata['name'] == 'Ice King':
        print('''You are now at the ice land, it is cold❄, quiet here... The Ice King takes control, nobody can survivle from this endless coldness.
Your hands are shaking, attack damage -1''')
        chardata['damage'] -= 1
        if chardata['name'] == 'Mage':
            print('Tips: Fire after fireballs no longer exist')
    if mondata['name'] == 'Lava King':
        print('''You are now at the kingdom of fire, the forever Lava Land. With the extreme heat here, the Lava King is growing...endlessly
Tips: The health of Lava King increases by 1 in every turn, defeat him as soon as possible.''')
        if chardata['name'] == 'Mage':
            print('Fortunately, because of the light form, your fire will still deal damage to the Lava King')
    if mondata['name'] == 'Tree of the Undead':
        print('''Vines come together to suffocate you as a formless entity spawns out of emptiness. Other wild creatures in the jungle flee
as the entity approaches you...
Tips: The health of Tree of the Undead increases by 1 in every turn, defeat him as soon as possible.''')
    if mondata['name'] == 'Wolf Pack':
        print('''A pack of wolves surround you... Having not eaten in a couple weeks, the pack fiercely stares into your eyes, and forces you 
into a corner. You are completely taken by surprise, attack damage -1''')
        chardata['damage'] -= 1
    if mondata['name'] == 'Corrupted Wizard':
        print('''A wizard appears out of thin air, holding a magic wand that seems to be cursed. He demonstrates just how powerful he is by
emitting a powerful beam at the ground. Smoke rises from the hole in the ground... The wizard is not here to mess around, attack damage -1''')
        chardata['damage'] -= 1
    if mondata['name'] == 'Skeleton Knight':
        print('''A galloping horse can be heard coming from a distance... One of the leaders of the undead army emerges into sight... He is here
to feed on human life.
Tips: The health of Skeleton Knight increases by 1 in every turn, defeat him as soon as possible.''')
    if mondata['name']=="TWILIGHT NAGA":
        print("A massive serpentine creature lurks in the shadow, its huge, bright yellow eyes shine in the darkness like a pair of gemstones")
        print("The creature slips into the light, revealing its huge snake-like appearance and bares its fangs") 
        print("The Ancient Beast, Naga, recognizes you as its prey")
        print("You are intimidated, attack damage -2")
        chardata["damage"]-=2
    if mondata['name']=="LICH KING":
        print("Ice and snow engulfs the room. You can feel the frost as it pierces through your bones...")
        print("Through the blizzard you spot a knight in black armour, sitting atop a throne of ice.")
        print("A pair of icy blue eyes emerges from within the helm, watching your every step.")
        print("The knight rises from its throne, manifesting its longsword")
        print("The Undead Knight, Lich King, recognizes you as its prey")
        print("Your movements are slowed, attack damage -2")
        chardata["damage"]-=2
    if mondata['name']=="FAFNIR THE DRAGON":
        print("One by one, torches illuminate the massive courtyard")
        print("A behemoth lays in slumber, atop a vault of riches spanning the whole yard")
        print("As you take a step forward, it snarls loudly")
        print("Its eyes fly open, the pair of ruby eyes penetrate your soul")
        print("The dragon rises, and spreads its wings, the dungeon shakes as it fights to contain it")
        print("The dragon roars. Magma spews from every inch of the courtyard")
        print("The Norse Dragon, Fafnir, has established its domain, health -4")
        chardata['health']-=4
    ability = 0
    burn = False
    while True:
                                                                                                        # Player's turn
        fightscreen(chardata,mondata,chardata["name"])
        ability += 1
                                                                                                         #VineGrasp and BerserkersRoar and VitalStrike and Fireball Start
        if ability == 2:
            if chardata['ability'] == 'VineGrasp':
                print(f'{mondata["name"]} has been trapped by roots! Skipped {mondata["name"]}\'s turn!  (VineGrasp)')
            if chardata['ability'] == 'BerserkersRoar':
                print('\"ROARRRRRR! I feel so POWERFUL💪!!!!!\" Damage+2 Health+2  (Berserker\'s Roar)')
                chardata['damage'] += 2
                chardata['health'] += 2
            if chardata['ability'] == 'VitalStrike':
                print('\"I am in the shadow...... Next attack do double damage🩸  (VitalStrike)\"')
                chardata['damage'] *= 2
            if chardata['ability'] == 'Fireball':                                                        #Fireball Starts and Ends
                burn = True
                print('\"Fireball!Burn burn burn!  (Fireball)\"')
                print('\"Look at those red stones...they are tiny...and become bigger and bigger! HaHaHa! Look above your head~\"')
                print('\"Booooooommm!💥\"')
                print(f'You\'ve dealt 3 damage to {mondata["name"]}')
                mondata["health"] -= 3
                ability = 0
                                                                                        #Player's Move
        print("Your Move:   [1]Attack        [2]Heal")
        move = input('>>>Enter: ')
        while move not in('1','2'):
            print("Invalid choice...Please Try Again.")
            move = input('>>>Enter: ')
        move = int(move)
        if move == 1: 
            mondata['health'] -= chardata['damage']
            print(f'You\'ve dealt {chardata["damage"]} damage to {mondata["name"]}')
        elif move == 2: 
            chardata['health'] += 3
            print(f'You\'ve healed yourself🩹. Health +3')
                                                                                        #BerserkersRoar and VitalStrike End
        if ability == 2: 
            if chardata['ability'] == 'BerserkersRoar': 
                chardata['damage'] -= 2
                ability = -1
            if chardata['ability'] == 'VitalStrike': 
                chardata['damage'] = int(chardata['damage']/2)
                ability = -1
                
        
        if mondata['health'] <= 0:  
            print(f'{mondata["name"]} has been defeated!')                                                    #Monster die
            monsters.remove(choice)
            return()
        
                                                                                        #Monster's turn
        fightscreen(chardata,mondata,mondata["name"])
                                                                                        #VineGrasp End
        if ability == 2 and chardata['ability'] == 'VineGrasp':
            ability = -1
            print(f'{mondata["name"]} got stunned💫')
            continue
        if burn == True and (ability == 0 or ability == 1) and mondata['name'] != 'Ice King':             #Fireball effect
            print(f'\"You are BBQing {mondata["name"]}!\"')
            print(f'The fire left on the ground is hurting {mondata["name"]}') 
            print(f'{mondata["name"]} Health -1')  
            mondata['health'] -= 1
            if mondata['health'] <= 0:
                monsters.remove(choice)
                return()                            
        if mondata['name'] == 'Lava King':
            print('\"I can feel my power is GROWING🔥!!!\" Lava King health +1') 
            mondata['health'] += 1
        if mondata['name'] == 'Tree of the Undead':
            print('\"The power of mothernature is on my side!!! I will not die today!" Tree of the Undead Health +1') 
            mondata['health'] += 1
        if mondata['name'] == 'Skeleton Knight':
            print('\"I shall not let these pesky humans get the better of me!!! I shall stop only when I end up victorious!" Skeleton Knight Health +1')
            mondata['health'] += 1
        chardata['health'] -= mondata['damage']     
        print(f'{mondata["name"]} attacks you, your health -{mondata["damage"]}')                                   
                                                                                        #Player die
        if chardata['health'] <= 0:
            print('''
D)ddddd   e)EEEE        a)      D)ddddd         
D)    dd  e)          a)  A     D)   dd
D)    dd  e)EEEE     a)AAAAAA   D)   dd 
D)    dd  e)        a)       A  D)   dd 
D)ddddd   e)EEEE   a)         A D)ddddd ''')   
            exit()
        input('>>>Enter Any Button to continue')

################################################################### Main() ###############################################################



def main():
    coin=0
    startorend = startscreen()
    if startorend == '2': return()
    difficulty = choosediff()
    if difficulty == '5': start = timer()
    chardata = choosecharacter()                                                    
    chardata = datadifficulty(difficulty,chardata)
    memhealth = chardata["health"]                                                  #Copy of chardata
    memdamage = chardata["damage"]
    monsters = ['mon1','mon2','mon3','mon4','mon5','mon6']                          #Monster's list             #Monster's data
    mondatas = {'mon1':{'damage': 3, 'health': 17, 'name': 'Wolf Pack'}, 'mon2':{'damage': 3, 'health': 18, 'name': 'Corrupted Wizard'}, 'mon3':{'damage': 2, 'health': 30, 'name': 'Tree of the Undead'}, 'mon4':{'damage': 2, 'health': 16, 'name': 'Skeleton Knight'}, 'mon5':{'damage': 2, 'health': 24, 'name': 'Ice King'}, 'mon6':{'damage': 5, 'health': 14, 'name': 'Lava King'}}
    for floor in range(4):
        mapdata = generate_map()
        playerpos1=5
        playerpos2=1
        while mapdata[playerpos1][playerpos2]!="O":
            move=input(">>>Enter your move(W/A/S/D): ")
            while checkmove(move,mapdata,playerpos1,playerpos2)==False:
                move=input(">>>Enter your move(W/A/S/D): ")
            mapdata[playerpos1][playerpos2]="·"
            playerpos1,playerpos2=checkmove(move,mapdata,playerpos1,playerpos2)
            if mapdata[playerpos1][playerpos2]=="M":
                fightmonster(monsters,mondatas,chardata)                                     #Starts monster fight screen
                chardata["damage"] = memdamage                                               #Reset char health and damage
                chardata["health"] = memhealth
            if mapdata[playerpos1][playerpos2]=="C":
                print("You have collected a coin! This may be useful later...")
                coin+=1
            if mapdata[playerpos1][playerpos2]=="O":
               
                print("You've entered a portal. Transferring to the next floor...")
                print("Your health has been replenished!")
            else:
                mapdata[playerpos1][playerpos2]="P"
                for z in mapdata:
                    print(''.join(z))
    chardata["health"] = memhealth
    chardata["damage"] = memdamage
    print("You enter a dark corridor...")                                                     #To boss level
    print("You creep down the hall, slowly...")
    print("The faint glow of light catches your eyes, seemingly from the end of the ominous tunnel")
    print("You reach the end. Your eyes trail upwards as the pair of torches illuminate the gargantuan steel door in front of you")
    print("Right as you place your hand on the cold, metallic gate, a voice startles you")
    print('A mysterious hooded figure emerges from the darkness')
    print('"A great challenge awaits you", it says. "You may need some assistance".')
    proceed="No"
    while proceed=="No" or proceed == 'no':
        print("Do you wish to trade with the hooded merchant?")
        trade=input(">>>Enter (Yes/No): ")
        while trade not in ("Yes","No","yes","no"):
            print("Invalid choice...Try again.")
            print("Do you wish to trade with the hooded merchant?")
            trade=input(">>>Enter (Yes/No): ")
        if trade=='Yes' or trade == 'yes':
            purchase=input(f'''
[={'-'*100}=]
Your coins: {coin}
Purchase an item: [1]Ares' Chestplate(Health) - 4 coins  [2]Odin's Blessing(Damage) - 3 coins  [3]Ring of Hestia(Health) - 2 coins  [4]Exit

>>>Enter: ''')
            if purchase=='1':
                if coin>=4:
                    print("You have purchased Ares' Chestplate! Your maximum health has increased by 8")
                    coin-=4
                    chardata["health"]+=10
                else:
                    print("Insufficient coins!")
            elif purchase=='2':
                if coin>=3:
                    print("Odin enchants your weapons! Your maximum damage has increased by 4")
                    coin-=3
                    chardata["damage"]+=4
                else:
                    print("Insufficient coins!")
            elif purchase=='3':
                if coin>=2:
                    print("The Ring of Hestia increases your vitality! Your maximum health has increased by 4")
                    coin-=2
                    chardata["health"]+=4
                else:
                    print("Insufficient coins!")
        print("Do you wish to proceed?(Yes/No)")
        proceed=input(">>>Enter: ")
        while proceed not in ("Yes","No","yes","no"):
            print("Invalid input...Please try again.")
            print("Do you wish to proceed?(Yes/No)")
            proceed=input(">>>Enter: ")

    print("I wish you good luck...")
    print("You pushed past the the heavy set of doors, revealing a massive, eerie courtyard...")
    boss=['boss1','boss2','boss3']
    bossdata={'boss1':{'damage': 2, 'health': 30, 'name': "TWILIGHT NAGA"}, 'boss2':{'damage': 3, 'health': 25, 'name': "LICH KING"}, 'boss3':{'damage': 4, 'health': 20, 'name': "FAFNIR THE DRAGON"}}
    fightmonster(boss,bossdata,chardata)
    print("As you step through the portal, you're met with the familiar breeze of the outside world")
    print("You feel the gentle touch of the lime green grass as you lay on your back, gazing at the skies above. You are home.")
    print("Congratulations! You have completed the game!")
    end = timer()
    if difficulty == '5': print(f'Time used: {round(((end - start)/60),5)} minutes')

main()





        
        

