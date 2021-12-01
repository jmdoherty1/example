import requests
from pprint import pprint
import random
import webbrowser
"""
------------------


"""


amountCards=2 #change value to test, usually 30
amountPlayers=2
deck_WildPokemon= []
deck_Player = []
r = random.choice #To shorten line length, make it readible
pokemonNum = []
y=1
while y < 151:
    pokemonNum.append(y)
    y+=1

KO_word_list=["fainted.", "was knocked-out.","became dizzy.","was stunned.","was KO_word_list-ed.",
              "collapsed.","fell to the floor with a thud.","fell to the ground in pain."]
catch_word_list_adv_word_list=["violently","gently", "quickly","slowly","carefully","carelessly",]
catch_word_list=["lob", "toss", "launch","hurl","throw","pitch","fling","aim","heave","sling"]
congrats_word_list=["Well done", "Nice job","Great job","Good job","Nice work","Great work",
                    "Good work", "Brilliant","Awesome","Cool"]

walkingIntro_word_list=["You begin to","You start to","You","You take you time and"]
walking_word_list=["potter","stroll","jog","wander","walk","ramble","mosey","roam","ride your bike","head"]
walkingPrepositions_word_list=["down to the","towards the","along the","across the","by the","near the","away from the"]
walkingLocations_word_list=["beach","shore","bushes","trees","grass","grasslands","wetlands","cave","hills", "mountains","village","houses","sandy dunes"]

def splashScreen():
    print("""
                                  ,'
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
""")
    input("Press 'Enter' when ever you see this: >")
    menu()

def menu():
    print("--------------")
    print("-----MENU-----")
    print("--------------")
    while True:
        print("1. Play")
        print("2. How to play")
        print("3. Pokemon Lore in the games")
        print("4. About this Python Project")
        print("5. Exit")
        menuSelection=input("\nPlease select an option using the number:")
        if menuSelection == "1":
            numOfCardsForGame()
        elif menuSelection == "2":
            howToPlay()
        elif menuSelection == "3":
            pokemonLore()
        elif menuSelection == "4":
            aboutPythonProject()
        elif menuSelection == "5":
            print("...Bye then")
            input(">")
            quit()
        else:
            print("Invalid Selection")

def howToPlay():
    print("\n-------------")
    print("-How to Play-")
    print("-------------")
    print("""
Aim of the Game:
Win the game by catching all of the different types pokemon.
Do this by fighting them. If you win the fight you will catch in a pokeball and be able to use them in future fights.
If your pokemon loses a fight, you lose that pokemon and need to catch that type again.
If you lose all of your pokemon, you lose the game.""")
    input(">")
    print("""
Set Up:
1.You select an even number of pokemon you wish to have in the game.
2.Half of the pokemon are yours and the other half are in the wild.""")
    input(">")
    print("""
Stages of the game are:
1. You encounter wild pokemon
2. You are given the option to research the pokemon
3. You can choose to run away or fight. 
3. You select one of the card's stats
3. Another random card is selected for your opponent (the computer)
4. The stats of the two cards are compared
5. The player with the stat higher than their opponent wins""")
    input(">")
    menu()

def pokemonLore():
    print("\n-------------")
    print("Pokemon  Lore")
    print("-------------")
    print("Pokemon means Pocket Monster...")
    input(">")
    menu()

def aboutPythonProject():
    print("\n-------------")
    print("-The Project-")
    print("-------------")
    print("It's a Python program...")
    input(">")
    menu()

def numOfCardsForGame():
    while True:
        try:
            amountCards = int(input("How many Pokemon do you want in the game?(Even numbers only)"))
            if amountCards % 2 == 0:
                building_deck(deck_WildPokemon,amountCards)
            else:
                print("Invalid selection")
        except:
            print("Invalid selection")

def building_deck(deck_WildPokemon,amountCards):
    print("\n---------------")
    print("You're late! You are currently grabbing random Pokeballs from your bedroom.")
    print("You'll be read to start you adventure in a second...")
    print("---------------")
    for x in range(amountCards):
        x+=1
        pokemonToDeck = r(pokemonNum)
        url = "https://pokeapi.co/api/v2/pokemon/{}/".format(pokemonToDeck)
        pokemonNum.remove(pokemonToDeck)
        data = requests.get(url)
        pokemon = data.json()
        deck_WildPokemon.append({"Card ": str(x), "Name":str.title(pokemon['name']),"Height":str(pokemon['height']/10),"Weight":str(pokemon['weight']/10),"Exp": pokemon["base_experience"],"Move": pokemon["abilities"][0]["ability"]["name"]} )
    print("YOU ARE READY!\nCatch as many Pokemon as you can!")
    deal_cards(amountCards,amountPlayers)

def deal_cards(amountCards,amountPlayers):
    cardsPerPlayer = int(amountCards / amountPlayers)
    print(cardsPerPlayer)
    for x in range(cardsPerPlayer):
        x += 1
        cardDealt = random.choice(deck_WildPokemon)
        deck_Player.append(cardDealt)
        deck_WildPokemon.remove(cardDealt)
    displayPokemonRemain()

def displayPokemonRemain():
    print("---------------")
    print ("YOU HAVE:",len(deck_Player), "POKEMON")
    print("YOU NEED:", len(deck_WildPokemon), "MORE POKEMON")
    print(input(">"))
    walking()

"""
print("TESTING: see the 15 pokemon in the wild and in the players hand after they are dealt")
print("TESTING:players pk:", deck_Player)
print("TESTING:in the wild:", deck_WildPokemon)
"""#TESTING

def walking():
    print("---------------")
    print(r(walkingIntro_word_list),r(walking_word_list),r(walkingPrepositions_word_list),r(walkingLocations_word_list)+".")
    print(input(">"))
    print("Suddenly...")
    print(input(">"))
    wildPokemonAppears()

def wildPokemonAppears():
    print("---------------\nA wild",deck_WildPokemon[0]["Name"],"appeared!\n--------------- ")
    while True:
        pokedexChoice = input("\nDo you want to use your Pokedex to research the pokemon? y/n")
        if pokedexChoice=="y":
            pokedex()
        elif pokedexChoice=="n":
            fight_or_flee()
        else:
            print ("Invaild selection")

def pokedex():
    webbrowser.open("https://www.pokemon.com/uk/pokedex/" + deck_WildPokemon[0]["Name"])
    fight_or_flee()

def fight_or_flee():
    while True:
        print("\nDo you want to fight the wild", deck_WildPokemon[0]["Name"] + "? y/n")
        fightOrFlight = input()
        if fightOrFlight == "y":
            playersNextPokemon()
        elif fightOrFlight=="n":
            print("You ran away...")
            deck_WildPokemon.append(deck_WildPokemon[0])
            deck_WildPokemon.remove(deck_WildPokemon[0])
            deck_Player.append(deck_Player[0])
            deck_Player.remove(deck_Player[0])
            displayPokemonRemain()
        else:
            print("Invalid selection")

def playersNextPokemon():
    print("---------------\nYOUR POKEMON:\n--------------- ")
    print("  Pokemon:",deck_Player[0]["Name"])
    print("Height(h):",deck_Player[0]["Height"]+"m")
    print("Weight(w):",deck_Player[0]["Weight"]+"kg")
    print("    Xp(x):",deck_Player[0]["Exp"])
    playerSelectsStat()

def playerSelectsStat():
    while True:
        selectCompare = input("Select a stat to compare to the against the wild Pokemon (h,w,x)")
        if selectCompare == "h":
            print("\nYou selected height.")
            print("Your",deck_Player[0]["Name"]+"'s height is", deck_Player[0]["Height"]+"m")
            print("The wild", deck_WildPokemon[0]["Name"] + "'s height is", deck_WildPokemon[0]["Height"] + "m")
            print(input(">"))
            comparingPokemon( deck_Player[0]["Height"], deck_WildPokemon[0]["Height"])
        elif selectCompare == "w":
            print("\nYou selected weight.")
            print("Your",deck_Player[0]["Name"]+" weigh's", deck_Player[0]["Weight"]+"kg")
            print("The wild", deck_WildPokemon[0]["Name"] + " weigh's", deck_WildPokemon[0]["Weight"] + "kg")
            print(input(">"))
            comparingPokemon(deck_Player[0]["Weight"], deck_WildPokemon[0]["Weight"])
        elif selectCompare == "x":
            print("\nYou selected Xp.")
            print("Your",deck_Player[0]["Name"] + " has", deck_Player[0]["Exp"] , "experience points!")
            print("The wild",deck_WildPokemon[0]["Name"] + " has", deck_WildPokemon[0]["Exp"], "experience points!")
            print(input(">"))
            comparingPokemon(deck_Player[0]["Exp"], deck_WildPokemon[0]["Exp"])
        else:
            print("Invalid selection")

def comparingPokemon (playersPokemon,wild): #LUCK HAS BEEN ADDED TO MAKE IT WINABLE
    print("---------------\nFight\n---------------")
    luck=random.randint(1,4)
    if luck == 1:
        print("You got lucky! The",deck_WildPokemon[0]["Name"],"got distracted!")
        playerwins()
    else:
        if playersPokemon >= wild:
            playerwins()
        else:
            playerloses()

def playerwins ():
    print ("\n"+deck_Player[0]["Name"], "used", deck_Player[0]["Move"]+". The wild", deck_WildPokemon[0]["Name"], r(KO_word_list))
    print("You",r(catch_word_list_adv_word_list),r(catch_word_list),"a pokeball at it and...",input(">"))
    print(r(congrats_word_list)+ "! You caught a", deck_WildPokemon[0]["Name"]+"!",input(">"))
    print ("You now have a",deck_WildPokemon[0]["Name"]+".",input(">"))
    print(input(">"))
    deck_Player.append(deck_WildPokemon[0])
    deck_Player.append(deck_Player[0])
    deck_WildPokemon.remove(deck_WildPokemon[0])
    deck_Player.remove(deck_Player[0])
    gameoverChecker()
#    print("TESTING: the wild pkmn should now be removed and add to players hand")
#    print("TESTING: players pkmn:",deck_Player)
#    print("TESTING: pkmn in the wild:", deck_WildPokemon)

def playerloses ():
    print (deck_Player[0]["Name"], "tried to use", deck_Player[0]["Move"]+" but The wild", deck_WildPokemon[0]["Name"], "dodged it!")
    print ("The", deck_WildPokemon[0]["Name"], "countered with", deck_WildPokemon[0]["Move"]+ "!",input(">"))
    print("Your",deck_Player[0]["Name"],r(KO_word_list),input(">"))
    print (deck_Player[0]["Name"]+" was sent Nurse Joy at the PokeCenter. It'll be released into the wild once it's healed.",input(">"))
    print ("You no longer have a",deck_Player[0]["Name"]+". You need to catch another one.",input(">"))
    input(">")
    deck_WildPokemon.append(deck_Player[0])
    deck_WildPokemon.append(deck_WildPokemon[0])
    deck_Player.remove(deck_Player[0])
    deck_WildPokemon.remove(deck_WildPokemon[0])
    gameoverChecker()
#    print ("TESTING: the player should have lost the fighting pokemon and it's now in the wild")
#    print ("TESTING: players pkmn:",deck_Player)
#    print ("TESTING: pkmn in the wild:", deck_WildPokemon)

def gameoverChecker():
    if len(deck_Player) == amountCards:
        print ("YOU DID IT! YOU CAUGHT ALL OF THE POKEMON!")
        print("YOU ARE A POKEMON MASTER!",input(">"))
        print("Bye...", input(">"))
        input(">")
        quit()
    elif len(deck_Player) == 0:
        print("You failed! You lost all of your Pokemon...")
        print("Go home and see if your Mum can get you a job in the village...",input(">"))
        print("Bye...",input(">"))
        input(">")
        quit()
    else:
        displayPokemonRemain()

splashScreen()