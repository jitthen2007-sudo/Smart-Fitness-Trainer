def calculate_bmi(weight, height):
    height_m = height / 100
    return round(weight / (height_m ** 2), 2)


def diet_plan(bmi, goal, preference):

    
    if bmi < 18.5:
        bmi_msg = "You are underweight. Increase calorie intake."
    elif bmi < 25:
        bmi_msg = "You are in a healthy range. Maintain your diet."
    else:
        bmi_msg = "You are overweight. Focus on weight loss."

    
    if goal == "lose":
        base = "Follow a low-calorie diet with more cardio."
    elif goal == "gain":
        base = "Follow a high-protein diet with calorie surplus."
    else:
        base = "Maintain a balanced diet."

   
    if preference == "veg":
        food = "Include paneer, lentils, nuts, fruits, and vegetables."
    else:
        food = "Include eggs, chicken, fish, milk, and protein-rich foods."

    return bmi_msg + "\n" + base + "\n" + food


def grocery_list(preference):
    if preference == "veg":
        return ["Rice", "Dal", "Paneer", "Vegetables", "Fruits", "Nuts"]
    else:
        return ["Chicken", "Eggs", "Fish", "Milk", "Rice", "Vegetables"]


def nutrition_tracker(calories):
    if calories < 1500:
        return "Low intake  Increase your calories."
    elif calories < 2500:
        return "Normal intake  Good job!"
    else:
        return "High intake  Control your diet."



if __name__ == "__main__":
    print("------ AI DIETICIAN & CALORIE COACH ------\n")

    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (cm): "))

    goal = input("Goal (lose/gain/maintain): ").lower().strip()
    preference = input("Diet (veg/nonveg): ").lower().strip().replace(" ", "")

    calories = int(input("Daily calories intake: "))

    bmi = calculate_bmi(weight, height)

    print("\n========== RESULT ==========\n")

    print("Your BMI:", bmi)

    print("\n Diet Plan:")
    print(diet_plan(bmi, goal, preference))

    print("\n Grocery List:")
    for item in grocery_list(preference):
        print("-", item)

    print("\n Nutrition Status:")
    print(nutrition_tracker(calories))