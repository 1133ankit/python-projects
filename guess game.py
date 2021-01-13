import random
print("please enter number between 0 to 10")
num = random.randint(0,10)
#create a score board
score = 0
while True :
    guess = input("enter a number")
    if guess == 'q':
        print("game over")
        break
        
    if guess == num:
        print("you won")
        print("your num is=",num)
        score = score +10
        print(score)
        
    else:
        print("you loose")
        print("your guess did not match")
        print("your num is ",num)
    
        
