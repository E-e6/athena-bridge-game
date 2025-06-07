import time
import random

score = 0

def intro():
    print("🛡️ Welcome to the Athena Award Second Code – Bridge of Brilliance!")
    print("You're a Roman engineer tasked with building a mighty bridge.")
    print("To succeed, solve puzzles and answer questions about Roman bridge technology.")
    input("Press Enter to begin your journey...")

def ask_question(question, options, correct_index):
    global score
    print("\n" + question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    try:
        answer = int(input("Your answer (1-4): "))
        if answer == correct_index + 1:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {options[correct_index]}")
    except:
        print("❌ Invalid input. Moving on.")

def puzzle_bridge_arch():
    print("\n🧱 PUZZLE: Build the arch!")
    print("You need to select the correct keystone shape to finish the arch.")
    print("Which stone shape will distribute weight best at the top of the arch?")
    print("1. Square\n2. Triangle\n3. Wedge\n4. Circle")
    choice = input("Your answer (1-4): ")
    if choice == "3":
        print("✅ Perfect! The wedge-shaped keystone locks the arch.")
        return True
    else:
        print("❌ Oh no! The arch collapsed.")
        return False

def stage_one():
    print("\n🔨 Stage 1: Planning the Foundations")
    ask_question(
        "What material did Romans use to make their bridges last underwater?",
        ["Brick mortar", "Lime plaster", "Pozzolanic concrete", "Marble paste"],
        2
    )

def stage_two():
    print("\n🏗️ Stage 2: Constructing the Arches")
    success = puzzle_bridge_arch()
    if success:
        global score
        score += 2
    else:
        print("You must reinforce your knowledge before proceeding!")

def stage_three():
    print("\n🛶 Stage 3: Final Touches")
    ask_question(
        "Which famous Roman aqueduct bridge still stands in France?",
        ["Pont Neuf", "Pont du Gard", "Ponte Vecchio", "Pont Alexandre III"],
        1
    )

def end_game():
    print("\n🎉 Congratulations, Roman Engineer!")
    print(f"🏛️ Your final score: {score}/5")
    if score >= 4:
        print("🌟 You have earned the Athena Award – Second Code!")
    else:
        print("🔁 Try again to master the ancient secrets of bridge building.")

# MAIN GAME LOOP
intro()
stage_one()
stage_two()
stage_three()
end_game()