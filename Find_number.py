#imports
import random;
import os;

#Fuctions
def clear():
    os.system('cls');

def check_level(level_Game):
    if level_Game =='e' :
      return 10
    elif level_Game == 'm' :
      return 100
    elif level_Game == 'h' :
       return 1000
    elif level_Game == 'g':
      return 10000
    else:
         print("option invalid")

#variaveis
level='';
low_number=1
high_Number=0;
plays=0;
player_number=0;
radom_number=0;

#start Game
print("Welcome, we will start a game\n");
print("rules: \t You Have to find the number from the computer\n\t the numbers must be positive and integer\n");

#check_input
while not high_Number:
    level=input("wich level do you wanna play? \nE-Easy, M-Mediu, H-Hard, G-Good :\n").lower();
    high_Number=check_level(level);

radom_number=random.randint(low_number, high_Number)

clear();

while player_number is not radom_number:

    player_number=input(f"pick a number between {low_number} and, {high_Number} \n")
    if player_number.isnumeric():

        plays+=1;
        player_number=int(player_number); #convert from str To int

        if player_number < radom_number:
            print("Sorry, not this time... your number is to low")
        elif player_number > radom_number:
            print("Sorry, not this time... your number is to high")

    else:
       print("sorry, input invalid");

print(f"congrats, you find the number in {plays}, plays\n\n")