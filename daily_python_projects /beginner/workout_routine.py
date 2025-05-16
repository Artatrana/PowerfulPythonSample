import random

# # Step 1: Define functions for different workout types
def get_cardio_exercise():
    return random.choice(["Jumping Jacks", "Burpees", "Running in Place", "Jump Rope", "High Knees"])

def get_strength_exercise():
    return random.choice(["Push-ups", "Squats", "Lunges", "Plank", "Dumbbell Press"])

def get_flexibility_exercise():
    return random.choice(["Yoga Stretch", "Hamstring Stretch", "Toe Touches", "Cat-Cow Stretch", "Shoulder Rolls"])

# Step 2: Ask user for workout preference
print("Welcome to the Workout Routine Generator! 🏋️‍♂️")
workout_type = input("Choose your workout type (cardio/strength/flexibility): ").strip().lower()

# Step 3: Suggest an exercise based on the input
if workout_type == "cardio":
    print(f"Try this exercise: {get_cardio_exercise()} 💓")
elif workout_type == "strength":
    print(f"Try this exercise: {get_strength_exercise()} 💪")
elif workout_type == "flexibility":
    print(f"Try this exercise: {get_flexibility_exercise()} 🧘")
else:
    print("Invalid choice! Please select cardio, strength, or flexibility.")

print("Stay active and keep moving! 🚀")

