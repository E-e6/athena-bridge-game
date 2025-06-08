import pygame
import time
import webbrowser
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Function to play sound
def play_sound(filename):
    try:
        pygame.mixer.Sound(filename).play()
    except:
        print("🔇 Sound file missing or unsupported!")

# Function to open intro image
def show_bridge_image():
    img_path = os.path.realpath("roman_bridge.jpg")
    webbrowser.open('file://' + img_path)

# Game Introduction
def intro():
    print("🌉 Welcome to the Athena Award – Bridge of Brilliance!")
    print("🛠️ Test your knowledge of Roman engineering and bridges.")
    show_bridge_image()
    input("Press Enter to begin your quest!\n")

# Quiz Questions
def ask_question(question, options, correct_index):
    print(f"\n❓ {question}")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    try:
        answer = int(input("Your answer (1-4): "))
        if answer == correct_index + 1:
            print("✅ Correct!")
            play_sound("correct.wav")
            time.sleep(1)
            return True
        else:
            print(f"❌ Incorrect. Correct answer: {options[correct_index]}")
            play_sound("wrong.wav")
            time.sleep(1)
            return False
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")
        return False

# Main Game Function
def main():
    intro()
    score = 0

    questions = [
        {
            "question": "What material did the Romans often use to build bridges?",
            "options": ["Wood", "Roman concrete", "Iron", "Marble"],
            "answer": 1
        },
        {
            "question": "What is the name of the most famous Roman aqueduct bridge in France?",
            "options": ["Pont du Gard", "Tiber Bridge", "Aqua Claudia", "Ponte Sant'Angelo"],
            "answer": 0
        },
        {
            "question": "Which feature was key to Roman bridge strength?",
            "options": ["Flat stones", "Steel cables", "Arches", "Wooden beams"],
            "answer": 2
        },
        {
            "question": "Roman bridges helped connect...",
            "options": ["Villages only", "Trade routes and military roads", "Castles", "None"],
            "answer": 1
        }
    ]

    for q in questions:
        correct = ask_question(q["question"], q["options"], q["answer"])
        if correct:
            score += 1

    print(f"\n🏁 Quiz Complete! Your final score: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 You are a true Roman Engineer!")
    elif score >= 2:
        print("🔧 Not bad! You’re on your way.")
    else:
        print("🧱 Time to study more about bridges!")

# Run the game
if __name__ == "__main__":
    main()