#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint
num=randint(1,100)
guesses=[]
count=1
print("Guessing Game \nGuess should be less than 1 or greater than 100 \nOn Your first turn, if guess is within 10 of the number, output WARM \nfarther than 10 away from the number, output COLD \nOn all subsequent turns, if a guess is closer to the number than the previous guess output 'WARMER' \nfarther from the number than the previous guess, output 'COLDER' \n")
while True:
    guesses.append(int(input('Enter Guess: ')))
    if guesses[-1] in range(1,101):
        if num in guesses:
            print(f'Guessed in {count} guesses')
            break 
        elif abs(guesses[0]-num)<10 and len(guesses)==1:
            a=abs(guesses[-1]-num)
            print('WARM')
            count+=1
            continue      
        elif abs(guesses[0]-num)>10 and len(guesses)==1:
            a=abs(guesses[-1]-num)
            print('COLD')
            count+=1
            continue
        elif abs(guesses[-1]-num)<a:
            a=abs(guesses[-1]-num)
            print('WARMER')
            count+=1
            continue
        elif abs(guesses[-1]-num)>a:
            a=abs(guesses[-1]-num)
            print('COLDER')
            count+=1
            continue
    else:
        print('OUT OF BOUNDS')
        guesses.pop(-1)
        continue
