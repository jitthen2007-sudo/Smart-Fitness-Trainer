def analyze_emotion(text):
    text = text.lower()

    if any(word in text for word in ["tired", "sad", "low", "exhausted"]):
        return "sad"

    elif any(word in text for word in ["happy", "good", "great", "excited"]):
        return "happy"

    elif any(word in text for word in ["lazy", "skip", "bored"]):
        return "unmotivated"

    else:
        return "neutral"


def chatbot_response(user_input):
    emotion = analyze_emotion(user_input)

    if emotion == "sad":
        return "You seem tired  Take rest or do light workout today."

    elif emotion == "happy":
        return "Great energy!  Try an intense workout today!"

    elif emotion == "unmotivated":
        return "Start small Even 10 mins workout helps!"

    else:
        return "Stay consistent and follow your fitness plan!"


if __name__ == "__main__":
    print("🤖 Virtual Gym Buddy Activated!\n")

    while True:
        user = input("You: ")

        if user.lower() == "exit":
            print("Bot: Stay fit! ")
            break

        print("Bot:", chatbot_response(user))