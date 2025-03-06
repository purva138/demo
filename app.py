# rock-paper-scissors-game
import random

u_points = 0
c_points = 0

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'q' to exit): ").lower()
    
    if user_choice == 'q':
        print("Final Score - You:", u_points, "Computer:", c_points)
        break   
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice, try again!")
        continue
    
    option = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(option)
    
    print(f"Computer chose: {comp_choice}")
    