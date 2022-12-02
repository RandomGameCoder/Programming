#Dice Simulator
import random
ch='y'
while ch.lower()=='y':
    print('Your Score is',random.randint(1,6))
    ch=input('Play Again (Y/N):')
