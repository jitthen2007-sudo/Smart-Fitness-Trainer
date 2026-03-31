def recommend_program(goal):
    if goal == "lose":
        return "Cardio + HIIT workouts"
    elif goal == "gain":
        return "Strength training + weight lifting"
    else:
        return "Balanced fitness routine"


def recommend_gym(location):
    gyms = {
        "bangalore": ["Cult Fit", "Gold's Gym", "Anytime Fitness"],
        "chennai": ["Slam Fitness", "Fitness One", "Gold's Gym"],
        "delhi": ["Anytime Fitness", "Cult Fit", "Gold's Gym"]
    }

    return gyms.get(location.lower(), ["Local Gym 1", "Local Gym 2"])


def fitness_challenge(level):
    if level < 5:
        return "Do 10 squats daily"
    elif level < 15:
        return "Do 20 pushups daily"
    else:
        return "Advanced workout challenge"


def analyze_history(score):
    if score < 50:
        return "You need improvement"
    elif score < 150:
        return "Good progress"
    else:
        return "Excellent performance"



if __name__ == "__main__":
    print("------ GYM RECOMMENDER & PLANNER ------\n")

    goal = input("Enter your goal (lose/gain/maintain): ").lower()
    location = input("Enter your city: ").lower()
    score = int(input("Enter your performance score: "))

    print("\n Workout Plan:", recommend_program(goal))

    print("\n Nearby Gyms:")
    for gym in recommend_gym(location):
        print("-", gym)

    print("\n Challenge:", fitness_challenge(score))

    print("\n Performance Analysis:", analyze_history(score))