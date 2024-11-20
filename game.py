import random
#S-1: defining the roll function using random module so we get a number generated
def roll():
    min=1
    max=6
    roll=random.randint(min,max)
    return roll
value=roll()
#S-2: Decding how many number of players will play
while True:
    players=input("Enter no.of players playing the game (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Enter number of players between 2 to 4!!")
    else:
        print("Enter Valid number!!") 

max_score=50
player_scores=[0 for _ in range(players)]  #list comprehension add 0 as score for number of players in the list

#main logic
while max(player_scores)<max_score:
    
    for player_idx in range(players):
        print(f"\nplayer {player_idx+1}'s turn has just started\n")
        print(f"Your current total = {player_scores[player_idx]}")
        current_score=0
     
        while True:  
         will_roll=input("Do you want to Roll the dice (y/n): \n").strip().lower()
         if will_roll!="y":
          break
         value=roll()
         if value==1:
          current_score=0
          print("\nYou rolled a 1!, Turn finished\n")
          break
         else:
          current_score+=value
          print(f"You rolled a, {value}")
        print(f"\nYour current score = {current_score}\n") 
        player_scores[player_idx]+=current_score
        print(f"Your current total: {player_scores[player_idx]}")
max_score=max(player_scores)
winner=player_scores.index(max_score)
print(f"Winner is Player {winner+1} with a score of {max_score}")                 


        
     