#this cs student codes hangman the old fashioned way

import random
words = ["james" , "myrrh" , "fatty" ,"annoying" , "this" ,"that"]
word = random.choice(words)
game = True




number = len(word)
underscores=[]
for i in range(number):
    underscores.append("_")


 
guess = []
lives = 6
letters = list(word)
while game:
    print("".join(underscores))
    user_input = input("type letter:")
    if not user_input:
        continue
    if user_input in word:
        for i in range(len(word)):
            if word[i] == user_input:
              underscores[i] = user_input
        print("".join(underscores))
    else:
       lives -= 1
       print(f"Letter was not in the word. lives remaining:{lives}")
    
    if "_" not in underscores:
        print(f"You won! The word was:{word}")
        game = False
   
    if  lives==0:
        print(f"You lost! The word was:{word}")
        game = False
