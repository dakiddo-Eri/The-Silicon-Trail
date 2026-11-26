import time
import sys
#dev notes for mee: sys.exit()
miles = 1000  #idk
cash = 500  #dolla dolla sign
sanity = 100  #percentage
hardware_hp = 100  #percentage
inventory = []
running = True

def end_game():
    print ("YA LOST, GAMEOVER, TRY AGAIN IF YA DARE")
    sys.exit()

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
time.sleep(1)
print("The global internet has collapsed into 'The Great AI takeover' ")
time.sleep(1)
print("")
