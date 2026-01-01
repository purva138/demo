# rock-paper-scissors-game
import random

u_points = 0
c_points = 0
round_no = 1

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'q' to exit): ").strip().lower()
    
    if user_choice == 'q':
        print("\n🏁 GAME OVER")
        print(f"Final Score → You 🧑: {u_points} | Computer 🤖: {c_points}")
        break   
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("❌ Invalid choice, try again!")
        continue
    
    option = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(option)
    
    print(f"\n🎯 Round {round_no}")
    print(f"🧑 You chose     : {user_choice}")
    print(f"🤖 Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        print("🤝 Result: It's a Tie!")
    elif (
        (user_choice == 'rock' and comp_choice == 'scissors') or
        (user_choice == 'scissors' and comp_choice == 'paper') or
        (user_choice == 'paper' and comp_choice == 'rock')
    ):
        print("🎉 Result: You Won!")
        u_points += 1
    else:
        print("😔 Result: You Lost!")
        c_points += 1

    # ✅ Better aligned score display
    print("\n📊 SCOREBOARD")
    print("-----------------------")
    print(f"🧑 You      : {u_points}")
    print(f"🤖 Computer : {c_points}")
    print("-----------------------\n")
    
    round_no += 1  # ✅ Increment round number

    replay = input("🔁 Play next round? (y/n): ").strip().lower()
    if replay != 'y':
        print("\n👋 Thanks for playing!")
        break