# made in python 3.12.6

# todo:
# 1. user friendly maken            [done](test dit nog)
# 2. help toevoegen                 [done]
# 3. boekje + word document invullen                [    ]
kamer = 0
current_position = "center"
current_options = []
inventory = []
open_deuren = []
gezecht = False
print("je wordt wakker, je bevint je in een kamer die je niet kent, je bent gekidnapt, maar door wie, je probeert de kamer te ontsnappen,\nhoe ga je dat doen?\n")

current_options = ["help", "lopen", "inspecteren","bekijk inventory"]
while True:
    if kamer == 2 and gezecht == False:
        print("\nfanboy: \"haha, welkom in mijn eindkamer,\nals je mijn geweldige puzzel oplost dan mag je gaan,\nmaar als je faalt moet je mijn game maken: het derde deel van mijn favorite portaal achtige spel serie\"\n")
        gezecht = True
    print("wat je wil je doen\nmaak hier je keuze, je opties zijn:  ")
    for index in range(len(current_options)):
        print(str(index + 1) + ".", current_options[index])
    user_input = input()
    if user_input == "lopen": # to do, toevoegen dat die de opties weergeeft van waar je naartoe kan
        user_input = input("welke kant op? \n1. links\n2. rechts\n3. muur rechts\n4. muur links\n5. muur voor\n6. muur achter\n")
        if user_input == "links":
            if kamer == 0:
                print("er is geen kamer links van je\n")
            else:
                print ("je loopt naar de kamer links van je") # moet nog gelimiteert worden zodat het alleen werkt als je naar die kamer kan omdat de deur misscien niet open is of omdat daar geen deur is
                kamer -= 1
                print("je bent nu in kamer", kamer + 1, "\n")
        elif user_input == "rechts":
            if kamer == 0 and "dmrk0" in open_deuren:
                print("je loopt naar de kamer rechts van je")# moet nog gelimiteert worden zodat het alleen werkt als je naar die kamer kan omdat de deur misscien niet open is of omdat daar geen deur is
                kamer += 1
                print("je bent nu in kamer", kamer + 1, "\n")
            elif kamer == 1 and "dmrk1" in open_deuren:
                print("je loopt naar de kamer rechts van je")
                kamer += 1
                print("je bent nu in kamer", kamer + 1)
            else:
                print("je kan nog niet naar de kamer rechts van je\n")
        elif user_input == "muur rechts":
            print("je loopt naar de muur rechts van je\n")
            current_position = "muur rechts"
        elif user_input == "muur links":
            print("je loopt naar de muur links van je\n")
            current_position = "muur links"
        elif user_input == "muur voor":
            print("je loopt naar de muur voor je\n")
            current_position = "muur voor"
        elif user_input == "muur achter":
            print("je loopt naar de muur achter je\n")
            current_position = "muur achter"
        else: 
            print("daar kan je niet heen.\n")
    elif user_input == "inspecteren":
        if kamer == 0:
            if current_position == "muur rechts":
                user_input = input("wat wil je inspecteren, je opties zijn:\n1. deur\n2. poster\n3. kluis\n")
                if user_input == "deur":
                    if "dmrk0" not in open_deuren:
                        if "smrk0" in inventory:
                            print("de deur is nu open\n")
                            open_deuren.append("dmrk0")
                            inventory.remove("smrk0")
                        else:
                            print("je kan de deur niet open maken. zoek de sleutel van deur muur rechts kamer 1\n")
                    else:
                        print("de deur is al open\n")
                elif user_input == "poster":
                    print("Het is een poster met een futuristische auto.\n")
                elif user_input == "kluis":
                    #print(inventory.index("sleutel kluis"))
                    if "sleutel kluis" in inventory:
                        inventory.append("smrk0")
                        print("je hebt nu de sleutel voor de deur\n")
                    else:
                        print("je hebt de sleutel niet voor de kluis.\n")   
            elif current_position == "muur links":
                print("wat wil je inspecteren, je opties zijn:")
                user_input = input("1. nachtkastje\n2. poster\n")
                if user_input == "nachtkastje":
                    inventory.append("sleutel kluis")
                    print("je hebt nu de sleutel voor de kluis\n")
                elif user_input == "poster":      
                    print("het is een poster met een logo van een bedrijf genaamd Aperture Science\n")
            elif current_position == "muur voor":
                print("wat wil je inspecteren, je opties zijn:")
                user_input = input("1. poster 1\n2. poster 2\n")
                if user_input == "Poster 1":
                    print("het is een poster van gast met 50% leven\n")
                elif user_input == "poster 2":      
                    print("het is een poster van een stoomige game launcher.\n")
            elif current_position == "muur achter":
                print("wat wil je inspecteren, je opties zijn:")
                user_input = input("1. bed\n")
                if user_input == "bed":
                    print("Een futuristische capsule die bedoelt is voor relaxen\n")
            else:
                print("er is momenteel niets wat je kan inspecteren\n")
        elif kamer == 1:
            if current_position == "muur rechts":
                user_input = input("wat wil je inspecteren, je opties zijn:\n1. deur\n2. poster\n3. lamp\n")
                if user_input == "deur":
                    if "dmrk1" not in open_deuren:
                        if "smrk1" in inventory:
                            print("je hebt de deur open gebroken, de deur is nu open.\n")
                            open_deuren.append("dmrk1")
                        else:
                            print("Een bijna kapotte deur met een codeslot, voer een code in:\n")
                            user_input = input("voer 4 cijferige code hier in:  ")
                            if user_input == "0000":
                                print("de deur is open.")
                                open_deuren.append("dmrk1")
                    else:
                        print("de deur is al open\n")
                elif user_input == "poster":
                    print("Het is een poster van \"space, space space, spaaaaaaaace\"\n")
                elif user_input == "lamp":
                    if "bijl" not in inventory:
                        inventory.append("smrk1")
                        print("je hebt een bijl gevondem onder de lamp, je hebt nu de bijl.\n")
                    else:
                        print("het is een mooie lamp.\n")   
            elif current_position == "muur links":
                print("wat wil je inspecteren, je opties is:")
                user_input = input("1. muur\n")
                if user_input == "muur":
                    print("Er zit een stok in de muur. je neemt de stok mee.\n")
                    inventory.append("stok")
            elif current_position == "muur voor":
                print("wat wil je inspecteren, je opties zijn:")
                user_input = input("1. muur\n2. sticky note\n")
                if user_input == "muur":
                    if "stok" in inventory and "hamerkop" in inventory:
                        print("met de stok en de hamerkop heb je een hamer gemaakt en de muur kapot gemaakt, je bent ontsnapt!:)\n")
                        break
                    else:
                        print("deze muur ziet er zwak uit.")
                elif user_input == "sticky note":      
                    print("het is een sticky note waar op staat \"reminder: deze muur is niet stevig, repareer hem\"\n")
            elif current_position == "muur achter":
                print("wat wil je inspecteren, je opties is:")
                user_input = input("1. nachtkastje\n")
                if user_input == "nachtkastje":
                    print("je hebt een hamerkop gevonden\n")
                    inventory.append("hamerkop")
            else:
                print("er is momenteel niets wat je kan inspecteren\n")
        elif kamer == 2:
            if current_position == "muur rechts":
                user_input = input("wat wil je inspecteren, je opties is:\n1. puzzel\n")
                if user_input == "puzzel":
                    if "puzzelstuk" not in inventory:
                        print("het is een puzzel die 1 stukje mist.\n") 
                    else:
                        print("het puzzelstukje past.\nfanboy: \"je hebt de puzzel opgelost, dus ik kom mijn belofte na, je mag gaan.\n")
                        break
            elif current_position == "muur links":
                print("wat wil je inspecteren, je opties is:")
                user_input = input("1. muur\n")
                if user_input == "muur":
                    print("hier is niets te vinden\n")
            elif current_position == "muur voor":
                print("wat wil je inspecteren, je opties zijn:")
                user_input = input("1. muur\n")
                if user_input == "muur":
                    print("het is een puzzelst-, oh nee, toch niet, het is maak een papiertje in de vorm van het puzzelstuk\n")
            elif current_position == "muur achter":
                print("wat wil je inspecteren, je opties is:")
                user_input = input("1. nachtkastje\n")
                if user_input == "nachtkastje":
                    print("je hebt de puzzelstuk gevonden op het nachtkastje.\n")
                    inventory.append("puzzelstuk")
            else:
                print("er is momenteel niets wat je kan inspecteren\n")
    elif user_input == "bekijk inventory":
        if len(inventory) != 0:
            for index in range(len(inventory)):
                print(str(index + 1) + ".", inventory[index])
            print("\n")
        else:
            print("je inventory is leeg\n")
    elif user_input == "help":
        if kamer == 0:
            print("je moet de sleutel vinden om naar de volgende kamer te gaan\n")
        elif kamer == 1:
            print("je moet een bijl vinden om de deur open te breken, de code raden of de muur slopen met een hamer\n")
        elif kamer == 2:
            print("je moet de puzzel oplossen om te ontsnappen.\n")

print("je hebt gewonnen, het spel is voorbij\n:)")