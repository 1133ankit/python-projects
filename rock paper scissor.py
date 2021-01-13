def get_winner(p1,p2):
    if p1=='rock' and p2=='paper':
        
        return "first player wins"
    elif p1=='scissor' and p2== "paper":
        return "first palyer wins"
    elif p1=='paper' and p2=='rock':
        return" first player wins"
    elif p1== "scissor" and p2=='rock':
        return" second player wins"
    elif p1== "rock" and p2=="scissor":
        return " first palyer wins"
    elif p1== "paper" and p2== "scissor":
        return "second player wins"
    else:
        return"its tie"
player1 = P1 = input('first player: rock,paper or scissor: ')
player2 =  p2 = input('second player: rock ,paper  or scissor: ')
print(get_winner(player1,player2))
