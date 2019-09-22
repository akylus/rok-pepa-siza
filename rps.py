import random
from winchecker import winchecker

print("Welcome to Akylus' RPS Game")
print("How many points do you need to play for?")
print("3 or 5 or 7?")
points = int(input())
if(points != 3 and points != 5 and points != 7):
    while(points != 3 and points != 5 and points != 7):
        print("Enter a proper value from given options")
        points = int(input())

count = [0,0]
cpuu = ['R','P','S']
while(max(count)<points):
    print("Enter your move: R is Rock, P is Paper and S is Scissors")
    playermove = input().upper()
    while(playermove != 'R' and playermove != 'P' and playermove != 'S'):
        print("Enter a proper value from given options")
        playermove = input().upper()
    # R is 1, P is 2 and S is 3
    if(playermove == 'R'):
        playermove = 1
    if(playermove == 'P'):
        playermove = 2
    if(playermove == 'S'):
        playermove = 3
    cpumove = random.randint(1,3)
    print("My move:",cpuu[cpumove-1])
    winner = winchecker(playermove,cpumove)
    if(winner != 2):
        count[winner] += 1
    print("Current Score: ")
    print("You\t" + "CPU")
    print(str(count[0]) + "\t" + str(count[1]))
if(count[0]>count[1]):
    print("Yay! You won!")
else:
    print("Oops. I won.")