#this cs student codes hangman the old fashioned way
#step 1: randomly choose a word from a list of words

import random
words = ["james" , "myrrh" , "fatty" ,"annoying" , "this" ,"that"]
word = random.choice(words)
game = True


#step 2: print the underscorses

number = len(word)
underscores=[]
for i in range(number):
    underscores.append("_")


#step 3: user inputs a letter. 
guess = []
letters = list(word)
while game:
    print(underscores)
    user_input = input("type letter:")
    if not user_input:
        continue
    if user_input in word:
        print("correct")
        for i in range(len(word)):
            if word[i] == user_input:
              underscores[i] = user_input
        print(underscores)
    else:
        print("wrong")
     #when do you win
    
    if "_" not in underscores:
        print(word, "win")
        game = False
dsadadkljadkos jaso
### WHY DOES IT USE THE OLD CODE FOR THE TERMINAL WHAT THE HELL