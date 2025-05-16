# Project Description
#This program helps you track your workout routines, sets, reps, and weights. It lets you add exercises, record your progress,
# and review past workouts. Perfect for gym users who want to log their progress.

class Exercise:
    def __init__(self, name):
        self.name = name
        self.sessions = []  # Stores tuples of (sets, reps, weight)

    def add_session(self, sets, reps, weight):
        """Logs a new workout session."""
        self.sessions.append((sets, reps, weight))

    def show_progress(self):
        """Displays all logged sessions for this exercise."""
        print(f"\nProgress for {self.name}:")
        for i, (sets, reps, weight) in enumerate(self.sessions, 1):
            print(f"Session {i}: {sets} sets of {reps} reps at {weight} kg")

    def __str__(self):
        return self.name


class GymTracker:
    def __init__(self):
        self.exercises = {}

    def add_exercise(self, name):
        """Adds a new exercise to track."""
        if name in self.exercises:
            print("Exercise already exists.")
        else:
            self.exercises[name] = Exercise(name)
            print(f"Added exercise: {name}")

    def log_workout(self, name, sets, reps, weight):
        """Logs a workout session for an existing exercise."""
        if name in self.exercises:
            self.exercises[name].add_session(sets, reps, weight)
            print(f"Logged {sets} sets of {reps} reps at {weight} kg for {name}")
        else:
            print("Exercise not found. Add it first.")

    def view_progress(self):
        """Displays progress for all exercises."""
        if not self.exercises:
            print("No exercises tracked yet.")
        else:
            for exercise in self.exercises.values():
                exercise.show_progress()


if __name__ == "__main__":
    tracker = GymTracker()

    while True:
        print("\n🏋️ Gym Tracker Options:")
        print("1. Add Exercise")
        print("2. Log Workout")
        print("3. View Progress")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter exercise name: ").strip().capitalize()
            tracker.add_exercise(name)

        elif choice == "2":
            name = input("Enter exercise name: ").strip().capitalize()
            sets = int(input("Enter number of sets: "))
            reps = int(input("Enter number of reps: "))
            weight = float(input("Enter weight in kg: "))
            tracker.log_workout(name, sets, reps, weight)

        elif choice == "3":
            tracker.view_progress()

        elif choice == "4":
            print("Stay strong! 💪 Exiting Gym Tracker.")
            break

        else:
            print("Invalid choice. Try again.")