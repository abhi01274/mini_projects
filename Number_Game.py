 
# Interactive Guess the Number Game 

"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
    Then ask you ( Player ) to guess the number and store as guess number

    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""
import random

inp1= int(input("Guess the number between 1-100 :> "))

inp2= random.randint(1,100)

if inp1==inp2:
    print("you win")
else:
    print("Computer wins")
"""
Challenge 2
    Print the secret number and guess number when Player loses using format function 
"""

print("the secret number is ",inp2)
print("your guess was ",inp1)


"""
Challenge 3
    Print too HIGH or too LOW messages for bad guesses using elif. 
"""

if inp1>inp2 or inp1>100:
    print("too HIGH")
elif inp2>inp1 or inp2<0:
    print("too LOW")


"""
Challenge 4
    Let people play again and again until he guesses the right secret number
"""
import random

while True:
    in1=int(input("enter the no between 1 to 10 :"))
    if not in1:
        break
    in2=random.randint(1,10)
    if in1==in2:
        print("win")
        break
    elif in1 != in2:
        print("lose")
    
        
    


"""
Challenge 5
Limit the number of guesses to maximum 6 tries 
"""
def play_again():
    try:
            for i in range(0,7):
                inp1=int(input("enter no"))
                inp2=random.randint(0,10)
                if not inp1:
                    break
                if inp1==inp2:
                    print("win")
                    p=input("enter p to play again or press enter to quit")
                    if not p:
                        break
                    if p=="p":
                        play_again()
                        break
                else:
                     p=6-i
                     print(p,"tries lft")
                     if p==0:
                         p=input("enter p to play again or press enter to quit")
                         if not p:
                             break
                         if p=="p":
                              play_again() 
    except Exception as e:
        print(e)
play_again()

"""
Challenge 7
    Catch when someone submits a non integer
"""




