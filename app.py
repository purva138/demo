# rock-paper-scissors-game
import random

u_points = 0
c_points = 0

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'q' to exit): ").strip().lower()
    
    if user_choice == 'q':
        print("Final Score - You:", u_points, "Computer:", c_points)
        break   
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice, try again!")
        continue
    
    option = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(option)
    
    print(f"Computer chose: {comp_choice}")
    if user_choice == comp_choice:
        print("It's a tie! 🤝🏻")
    elif(user_choice == 'rock' and comp_choice == 'scissors'):
        print("Congratulations! You Won!! 🎉")
        u_points += 1
    elif(user_choice == 'scissors' and comp_choice == 'paper'):
        print("Congratulations! You Won!! 🎉")
        u_points += 1
    elif(user_choice == 'paper' and comp_choice == 'rock'):
        print("Congratulations! You Won!! 🎉")
        u_points += 1
    else:
        print("Oops! You Lose 😔")
        c_points += 1
    
    print(f"Score - You: {u_points}, Computer: {c_points}\n")
    
    replay = input("Do you want to play again? (y/n): ").lower().strip()
    if replay != 'y':
        print("Thanks for playing! 👋")
        break