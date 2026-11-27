import time
import sys
import random
#dev notes for mee: sys.exit()
miles = 1000  #idk
cash = 500  #dolla dolla sign
sanity = 100  #percentage
hardware_hp = 100  #percentage
running = True
inventory = []
pace = []


def win_game():
    print("winner winner chiken dinner, ya save the world in a very tottaly hard game yay!")
    time.sleep(7)
    sys.exit()

def end_game():
    print ("YA LOST, GAMEOVER, TRY AGAIN IF YA DARE")
    time.sleep(7)
    sys.exit()

def check_stats():
    global miles
    global inventory
    miles -= 20
    if miles < 0:
        miles = 5
    print(str(miles) + " miles left")
    print("$" + str(cash))
    print("%" + str(sanity) + " sanity")
    print("%" + str(hardware_hp) + " hardware hp")
    print("Inventory:")
    print(inventory)
    if hardware_hp <= 0:
        print("yo car broke down and you get shot by ChatGPT")
        end_game()
    elif sanity <= 0:
        print("you go crazy and you die in a hole")
        end_game()
    elif cash <= 0:
        print("you go broke and you cant buy gas, you die from ligma")
        end_game()
    else:
        print("onwards you go!!")

print("The Silicon Trail")
time.sleep(0.4)
print("Start?   y / n")
start = input(">")

if start == "n":
    print("exiting...")
    sys.exit()

else:
    print("startinggg...")

time.sleep(2)
print("The Year is 2029")
time.sleep(2)
print("The global internet has collapsed into 'The Great AI takeover' ")
time.sleep(2)
print("Every cloud server on Earth is now set on to just power AI models")
time.sleep(2)
print("Just recently, an AI model hallucinated and shut down every")
time.sleep(2)
print("health service in America")
time.sleep(2)
print("You are driving in an RGB-lit Honda Civic from Sacramento to")
time.sleep(2)
print("Silicon Valley, your task is to put in a high-cost, 32 GB DDR6 stick of RAM")
time.sleep(2)
print("into a health datacenter")
time.sleep(2)
print ("continue?")
s0 = input(">")
time.sleep(2)
print ("let the hardships begin...")
time.sleep(1)
print("Here are your stats")
time.sleep(1)
miles += 20
check_stats()#break 1
time.sleep(4)
print("here, want some contraband?? ")
time.sleep(1)
print("""
[1] White Monster, $30
[2] Anime Figure, $60
[3] Poppy's skibidi car lotion, $200
""")
time.sleep(1)
print("enter numbers, 1, 2, 3...")
while True:
    s1 = input(">")
    if s1 == "1":
        cash -= 30
        inventory.append("White_Monster")
        print("Brought 'White Monster' ")
        break
    elif s1 == "2":
        cash -= 60
        inventory.append ("Anime_Figure")
        print("Brought 'Anime_Figure")
        break
    elif s1 == "3":
        cash -= 200
        inventory.append ("Poppy's_Skibidi_Car_Lotion")
        print("Brought 'Poppy's Skibidi Car Lotion' ")
        break
    else:
        print("invalid input, try again boii")

print(str(miles) + " miles left")
print("$" + str(cash))
print("%" + str(sanity) + " sanity")
print("%" + str(hardware_hp) + " hardware hp")
print("Inventory:")
print(inventory)

time.sleep(3)
print("Driving on the highway, a rogue AI tollbooth blocks I-80. Its screen")
print("flickers with a smug ASCII face: ")
time.sleep(2)
print("Pay the RAM TAX, FLESH CREATURE, OR ANSWER MAH RIDDLE")
time.sleep(2)
print("""
[1] Give the 32 GB of DDR6 RAM
[2] Attempt to aruge it out in Python
[3] Full throtle that gas!!!
[4] Answer riddle
""")
print("enter number, eg. 1, 2, 3 ...")

while True:
    s1 = input(">")
    if s1 == "1":
        print("bro.. you might want to check your brain again man")
        end_game()
    elif s1 == "2":
        print("You argue it out in Python about semi-colons, you lose a" \
        "day worth of time and some of your sanity")
        sanity -= 20
        break
    elif s1 == "3":
        print("You punch that pedal and you bust through the gate." \
        "You're feeling great, but your car takes some damage...")
        hardware_hp -= 25
        sanity += 15
        break
    elif s1 == "4":
        print("What gets wet while drying?")
        time.sleep(1)
        print("""
        [1] A Sponge
        [2] An Ice Cube
        [3] A Towel
        """)
        s1 = input(">")
        if s1 == "1":
            cash -= 100
            print("nah, ya lose money")
            break
        elif s1 == "2":
            cash -= 100
            print("nah, ya lose money")
            break
        elif s1 == "3":
            cash += 15
            print("yup, yur correct, heres some money to compensate")
            break
    else:
        print("invalid, try again")

time.sleep(2)
check_stats()
time.sleep(3)
print("continue?")
input(">")

time.sleep(1)
print("You pull into a flickering gas station in the middle of nowhere." \
"Inside, a guy wearing three hoodies is selling contraband out of a trench coat." \
"You are dead tired from that drive.")
time.sleep(7)
print("""
[1] Buy 2x White Monster Drink, $15
[2] Buy mysterious 'overclocked thermal paste' for your Civic, $40
[3] Steal a dashboard Anime Figure and sprint
""")

print("enter number, eg. 1, 2, 3...")
while True:
    s1 = input(">")
    if s1 == "1":
        cash -= 15
        miles -= 15
        inventory.append("White_Monster")
        print("you will go another 15 miles tonight, yay!")
        break
    elif s1 == "2":
        if cash <= 40:
            print("ya too broke for that")
            continue
        cash -= 40
        outcome = random.choice(["good", "bad"])
        if outcome == "good":
            hardware_hp += 30
            print("sussy thermal paste worked!! yay")
        else:
            hardware_hp -= 30
            print("oh no... thats definetly mayonnaise, thermal paste no wok :( " \
            "your car breaks down even more")
        break 
    elif s1 == "3":
        outcome = random.choice(["good", "bad"])
        if outcome == "good":
            inventory.append("Anime_Figure")
            sanity += 20 
            print("you pull a succesful heist and you gain 'Anime_Figure' plus sanity")
            break
        else:
            sanity /= 2
            cash /= 2
            print("you are caught and you lose half yo sanity and money")
            break
    else:
        print("invalid choice, pick again boii")

time.sleep(2)
miles -= 30
check_stats()
time.sleep(4)
print("You continue on to that datacenter!")
time.sleep(1)
print("As you're driving on the highway, a truck covered with Anime and Arch" \
"sticker boxes you on the highway. A window rolls down and a Discord Mod yells:")
print("'NO MEMES IN GENERAL, GIVE ME YOUR FOOD NOW!!'")
time.sleep(7)
print("""
[1] Bribe him with White Monster
[2] Pull out mechanical keyboard and spam ping '@everyone'
[3] Attempt to explain the lore of your trip
""")
print("enter number, eg. 1, 2, 3...")

while True:
    s1 = input(">")
    if s1 == "1":
        if "White_Monster" in inventory:
            inventory.remove("White_Monster")
            print("Discord Mod nods respectfully and lets you pass.")
            print("heres yo inventory")
            time.sleep(1)
            print(inventory)
            break
        else:
            print("no 'White_Monster' in inventory, try again")
    elif s1 == "2":
        print("Discord Mod bans you from the highway and you have to back track")
        time.sleep(1)
        sanity -= 20
        miles += 20
        print("-20 sanity & + 20 miles")
        break
    elif s1 == "3":
        print("Discord Mod shoots a gun at your for no reason...")
        end_game()
        break
    else:
        print("try again")
time.sleep(4)
check_stats()
time.sleep(4)
print("You pick up a hitchhiker who refuses to stop talking about his" \
" 'revolutionary blockchain-powered toaster'. You are about to go crazy" \
" from his slander.")
time.sleep(7)
print("""
[1] Let him invest $100 of your trip money
[2] Throw your 'Anime Figure' out the window as a distraction
[3] Endure the lecture until the next exit
""")
print("enter number, eg. 1, 2, 3...")
while True:
    s1 = input(">")
    if s1 == "1":
        if cash <= 100:
            print("you're too broke...")
        else:
            cash -= 100
            outcome = random.choice(["good", "bad"])
            if outcome == "good":
                cash += 400
                sanity += 15
                print("i guess it did work!!")
                break
            else:
                print("ya lose that 1 hundo, sorry man...")
                break
    elif s1 == "2":
        if "Anime_Figure" in inventory:
            inventory.remove("Anime_Figure")
            sanity += 30
            print("it works yay, plus sanity for you")
            break
        else:
            print("no 'Anime_Figure' in inventory :(")
    elif s1 == "3":
        sanity -= 35
        print("Pure psychological damage")
        break
    else:
        print("invalid choice, pick again boii")
time.sleep(4)
check_stats()
time.sleep(4)
print("Your dashboard is glowing bright red and smelling" \
" like burnt toast. If you don't cool it down, the car will explode.")
time.sleep(4)
print("""
[1] Open all windows and drive 110 MPH
[2] Pour your coffee onto it
[3] Overclock yo car
[4] Shift gear from neutral to drive constantly
[5] Cry and put your tears on the dashboard
""")
print("choose number, 1, 2, 3...")
while True:
    s1 = input(">")
    if s1 == "1":
        outcome = random.choice(["good", "bad"])
        if outcome == "good":
            miles -= 450
            print("ayy it works, noice!")
            break
        else:
            hardware_hp -= 70
            print("the engine blow, so sorry man...")
            break
    elif s1 == "2":
        print("you attempt to pour your morning coffee on the dashboard...")
        time.sleep(1.5)
        print("your car blows up and you get ran over by a flying wheel")
        end_game()
    elif s1 == "3":
        print("you overclock your car's fans")
        time.sleep(1)
        print("the fans blow out and you crash into a lake")
        end_game()
    elif s1 == "4":
        print("you try to shift between neutral and drive gears constantly," \
        " the car does a 360 no scope on a passing duck and it flies into an" \
        " electrical pole")
        end_game()
    elif s1 == "5":
        print("you cry and the tears fall on your dashboard, the dashboard" \
        " somehow magically stops glowing red")
        break
    else:
        print("invalid choice, pick again boii")
time.sleep(4)
check_stats()
print("admin check...")
if "Poppy's_Skibidi_Car_Lotion" in inventory:
    while True:
        print("Use 'Poppy's Skibidi Car Lotion' ???")
        print("""
        [1] yess sirr
        [2] no, eww...
        """)
        s1 = input(">")
        if s1 == "1":
            inventory.remove("Poppy's_Skibidi_Car_Lotion")
            hardware_hp += 200
            print("added 200 health to ya car, ur prob set for the game!!")
            break 
        elif s1 == "2":
            print("no buy...")
            break
        else:
            print("invalid input, try again boii")

time.sleep(4)
print("You are approcahing Silicon Valley, a bunch of random dudes " \
" with pitch forks are blocking the road. What will you do...")
time.sleep(4)
print("""
[1] HIT THE GAS!! LET ME THROUGH!!!!
[2] Negotiate with the pitchfork dudes
[3] No mercy, unleash the hitchhiker
[4] Get out of the car with your stick of DDR6 RAM
[5] Turn back and full speed away
[6] Give 'em that stick o RAM
""")
print("choose a number, eg. 1, 2, 3...")
while True:
    s1 = input(">")
    if s1 == "1":
        print("you run 220 MPH through the crowd...")
        time.sleep(2)
        print("a pitchfork pierces through a window and hits you...")
        end_game()
    elif s1 == "2":
        print("you walk out of your car and immedietly get jumped...")
        end_game()
    elif s1 == "3":
        print("the hitchhiker walks out of the car, everyone immedietly jumps him" \
        " and you drive away quickly")
        print("apparently, you were housing Ram Altman in your car the entire time...")
        miles -= 200
        break
    elif s1 == "4":
        print("you're not out of your car yet, but pulling out that stick of RAM " \
        " makes you black out instantly, to never wake again...")
        end_game()
    elif s1 == "5":
        print("you turn arround and head back home as fast as you can...")
        print("You fail your mission... such sadness")
        end_game()
    elif s1 == "6":
        print("you give them that stick of ram, they fight over it allowing" \
        " your escape..")
        time.sleep(1)
        print("hehehe.... its a piece of plastic")
        break
    else:
        print("invalid input, try again")
time.sleep(4)
check_stats()
time.sleep(5)

print("here comes the long stretch, here pick an item of your choice")
time.sleep(2)
print("""
[1] White Monster
[2] Poppy's Skibidi Car Lotion
[3] Weird Looking Rock
[4] Thigh-High Socks
[5] Kawaii Glock
[6] Anime Figure
[7] Car Buff (instant)
[8] Sanity Buff (instant)
[9] +1 Cash (instant)
""")
print("(instant) means it will be applied RIGHT NOW!!")
print("enter a number, eg. 1, 2, 3...")

while True:
    s1 = input(">")
    if s1 == "1":
        inventory.append("White_Monster")
        print("Added `White Monster` to inventory, yay!")
        break
    elif s1 == "2":
        inventory.append("Poppy's_Skibidi_Car_Lotion")
        print("Added `Poppy's Skibidi Car lotion` to inventory, yay!")
        break
    elif s1 == "3":
        inventory.append("Weird_Looking_Rock")
        print("Added `Weird Looking Rock` to inventory, yay! ")
        break
    elif s1 == "4":
        inventory.append("Thigh_High_Socks")
        print("Added `Thigh High Socks` to inventory, yay!")
        break
    elif s1 == "5":
        inventory.append("Kawaii_Glock")
        print("Added `Kawaii Glock` to inventory, yay!")
        break
    elif s1 == "6":
        inventory.append("Anime_Figure")
        print("Added `Anime Figure` to inventory, yay!")
        break
    elif s1 == "7":
        hardware_hp += 20
        print("added %20 health to car!!")
        break
    elif s1 == "8":
        sanity += 20
        print("added %20 sanity to YOU!!")
        break
    elif s1 == "9":
        cash += 1
        print("added $1 to your ballance, you might want to check your brain again...")
        break
    else:
        print("invalid input, try again")
time.sleep(2)
print("now, choose your pace...")
time.sleep(1)
print("""
[1] Normal, keep your current pace
[2] Floor it the rest of the way
[3] Slowwww, prob torture for YOU
[4] Risk it, you can either get instant fast, or kaboom
""")

while True:
    s1 = input(">")
    if s1 == "1":
        pace = "normal"
        break
    elif s1 == "2":
        pace = "floor_it"
        break
    elif s1 == "3":
        pace = "slow"
        break
    elif s1 == "4":
        outcome = random.choice (["good", "bad", "bad"])
        if outcome == "good":
            cash += 40
            miles -= 40
            sanity += 15
            pace = "normal"
            print("you get $40, you run an extra 40 miles, and increase yo sanity by %15")
            break
        elif outcome == "bad":
            cash -= 40
            miles += 40
            sanity -= 15
            pace = "normal"
            print("you lose $40, you backtrack 40 miles, and you lose %15 sanity")    
            break
    else:
        print("invalid input, try again boii")

while miles > 25:
    if pace == "normal":
        miles -= 100
        print("Cruising steadily down I-80...")
    elif pace == "floor_it":
        miles -= 180
        hardware_hp -= 15
        sanity -= 10
        print("Redlining the Civic at 130 MPH! The engine is screaming...")
    elif pace == "slow":
        miles -= 40
        sanity -= 20
        print("Driving 35 MPH in the slow lane... everyone is honking at you...")
        time.sleep(3)     
    check_stats()
    time.sleep(2)
    if miles <= 25:
        break
    event = random.choice(["rock_event", "sock_event", "drone_trap"])

    if event == "rock_event":
        print("A rogue Boston Dynamics robodog jumps onto your hood!")
        print("""
[1] Throw 'Weird Looking Rock' at it
[2] Swerve violently
        """)
        while True:
            choice = input(">")
            if choice == "1":
                if "Weird_Looking_Rock" in inventory:
                    inventory.remove("Weird_Looking_Rock")
                    cash += 60
                    print("BONK! Direct hit. You aquire $60 worth of scrap from it")
                    break
                else:
                    print("ya no have that in inventory, try again...")
            elif choice == "2":
                hardware_hp -= 20
                print("You shake it off, but scrape the guardrail, ya drop 20 hardware hp")
                break
            else:
                print("invalid input, try again boii")
    elif event == "sock_event":
        print("Your Civic's onboard demands a firmware update in Rust!")
        print("""
[1] Equip 'Thigh High Socks' for +999 coding aura
[2] Smash the dashboard screen
""")    
        while True:
            choice = input(">")
            if choice == "1":
                if "Thigh_High_Socks" in inventory:
                    sanity += 25
                    miles -= 60
                    print("Instant 10x dev powers, you optimized the engine,")
                    break
                else:
                    print("ya dont have that in y o inventory, try again")
            elif choice == "2":
                hardware_hp -= 25
                sanity -= 15
                print("screen shattered, now you're driving without your gas meter")
                break
            else:
                print("invalid input, try again boii")

    elif event == "drone_trap":
        print("An Amazon delivery drone hovers in front of you windshield, demanding a tip")
        time.sleep(2)
        print("""
[1] Tip it 200
[2] Flash the 'Kawaii Glock'
[3] Ignore it
""")
        while True:
            choice = input(">")
            if choice == "1":
                cash -= 200
                print("It drops a complimentary air freshener and flies away")
                break
            elif choice == "2":
                if "Kawaii_Glock" in inventory:
                    cash += 50
                    sanity += 15
                    print("The drone panics, drops its package ($50) and flees")
                    break
                else:
                    print("No Kwaii Glock in inventory, pick again boii")
            elif choice == "3":
                hardware_hp -= 15
                print("It drops a brick on your hood out of spite, yo car takes damage")
                break
            else:
                print("invalid input, try again boii")

miles = 25
check_stats()
print("You are approaching the datacenter, all your hardwork is about" \
" to be paid off, an agent with your beautiful early access RTX 6060" \
" is already standing there")
time.sleep(5)
print("Some dude in a black coat comes up to you away from sight of the" \
" agent...")
time.sleep(3)
print("He tells you to give him that stick of RAM and you + him together can" \
" desktroy all datacenters, to make a new technological future...")
time.sleep(3.5)
print("""
[1] Give him it...
[2] Do the griddy on him and run to the datacenter...
""")
time.sleep(2)
print("enter number, eg. 1, 2, 3...   good luck man...")
while True:
    s1 = input(">")
    if s1 == "1":
        print("you jab the RAM at him, he nods at your and says," \
        " 'scammer gets scammed boii', and dissapears out of thin air")
        end_game()
    elif s1 == "2":
        print("he is agasted and dissapears into the shadows, you put" \
        " that RAM into the slot, all health service in America is now" \
        " restored...")
        time.sleep(4)
        print("Look at that! You're on the national news and you got a" \
        " RTX 6060 while you're at it!")
        win_game()
    else:
        print("invalid input, try again boii...")
time.sleep(2)
