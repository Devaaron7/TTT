# Starter Rock Paper Scissors Game where a tie results in a replay

# Note - All answers need to be lowercase and spelled correctly!

# Random Module used so Computer can pick 1 of 3 choices - Rock , Paper or Scissors
import random
import winsound
import time
from playsound import playsound

# This area has the code to show the Gif files for a certain win/lose/tie situation




# Games code is defined as a function called "Game". This allows the tie outcome to call game()..
# ..which restarts the code.

def game1():
    winsound.PlaySound(None, winsound.SND_ASYNC)
    winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\intense.wav", winsound.SND_ASYNC)
    print ("Rock, Paper, Scissors?\n\r")
    hanswer = input ("Type your answer\n\r")
    choices = ["rock", "paper", "scissors"]
    canswer = random.choice(choices)
    playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\tie.wav", True)
    print("                 \n\r")
    print("Rock\n\r")
    time.sleep(1)
    print("Paper..\n\r")
    time.sleep(1)
    print("Scissors...!\n\r")
    time.sleep(1)
    print("Shoot!!!\n\r")
    time.sleep(2)
    print("You Choose:", hanswer.lower() , "...And I Choose:", canswer.lower())
# This area defines winning Conditions for each choice:
    if hanswer.lower() == "rock" and canswer == "paper":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\dio.wav", winsound.SND_ASYNC)
        print("Paper beats Rock! I Win")
        time.sleep(3)
        playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\lose.wav", True)
    if hanswer.lower() == "rock" and canswer == "scissors":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\umad.wav", winsound.SND_ASYNC)
        print("Rock beats Scissors....I Lost..")
        playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\win.wav", True)
    if hanswer.lower() == "paper" and canswer == "scissors":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\dio.wav", winsound.SND_ASYNC)
        print("Scissors beats paper!! I Win")
        time.sleep(3)
        playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\lose.wav", True)
    if hanswer.lower() == "paper" and canswer == "rock":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\umad.wav", winsound.SND_ASYNC)
        print("Paper beats rock....I Lost..")
        playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\win.wav", True)
    if hanswer.lower() == "scissors" and canswer == "rock":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\dio.wav", winsound.SND_ASYNC)
        print("Rock beats scissors! I Win")
        time.sleep(3)
        playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\lose.wav", True)
    if hanswer.lower() == "scissors" and canswer == "paper":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\umad.wav", winsound.SND_ASYNC)
        print("Scissors beats paper...how...how did I Lose!!!??")
        playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\win.wav", True)
# This area defines a Tie
    if hanswer.lower() == canswer:
        print("It's a Tie!")
        print("Lets go again \n")
        return game1()

def game():
    winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\sf4train.wav", winsound.SND_ASYNC)
    print ("Rock, Paper, Scissors?\n\r")
    hanswer = input ("Type your answer\n\r")
    choices = ["rock", "paper", "scissors"]
    canswer = random.choice(choices)
    playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\wait.wav", True)
    print("                 \n\r")
    print("Rock\n\r")
    time.sleep(1)
    print("Paper..\n\r")
    time.sleep(1)
    print("Scissors...!\n\r")
    time.sleep(1)
    print("Shoot!!!\n\r")
    time.sleep(2)
    print("You Choose:", hanswer.lower() , "...And I Choose:", canswer.lower())
# This area defines winning Conditions for each choice:
    if hanswer.lower() == "rock" and canswer == "paper":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\dio.wav", winsound.SND_ASYNC)
        print("Paper beats Rock! I Win")
        time.sleep(3)
        playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\lose.wav", True)
    if hanswer.lower() == "rock" and canswer == "scissors":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\umad.wav", winsound.SND_ASYNC)
        print("Rock beats Scissors....I Lost..")
        playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\win.wav", True)
    if hanswer.lower() == "paper" and canswer == "scissors":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\dio.wav", winsound.SND_ASYNC)
        print("Scissors beats paper!! I Win")
        time.sleep(3)
        playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\lose.wav", True)
    if hanswer.lower() == "paper" and canswer == "rock":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\umad.wav", winsound.SND_ASYNC)
        print("Paper beats rock....I Lost..")
        playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\win.wav", True)
    if hanswer.lower() == "scissors" and canswer == "rock":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\dio.wav", winsound.SND_ASYNC)
        print("Rock beats scissors! I Win")
        time.sleep(3)
        playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\lose.wav", True)
    if hanswer.lower() == "scissors" and canswer == "paper":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\umad.wav", winsound.SND_ASYNC)
        print("Scissors beats paper...how...how did I Lose!!!??")
        playsound(r"C:\Users\Office\Desktop\Collected Projects\Rock Paper Scissors\music\win.wav", True)
# This area defines a Tie
    if hanswer.lower() == canswer:
        print("It's a Tie!")
        print("Lets go again \n")
        return game1()



# This function call starts the code within game(). 
game()

# This keeps window open after main code is completed, until you hit a key
input("Press Enter to Close the window")
