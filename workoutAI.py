import cv2
import mediapipe as mp
import numpy as np
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

def speak(text):
    engine.say(text)
    engine.runAndWait()

mp_pose = mp.solutions.pose

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = (
        np.arctan2(c[1]-b[1], c[0]-b[0]) -
        np.arctan2(a[1]-b[1], a[0]-b[0])
    )

    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180:
        angle = 360 - angle

    return angle

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

counter = 0
stage = None
prev_feedback = ""
performance_history = []

with mp_pose.Pose(min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as pose:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        feedback = ""
        suggestion = ""
        habit_msg = ""
        schedule = ""
        angle = 0

        try:
            landmarks = results.pose_landmarks.landmark

            hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                   landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

            knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

            ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

            angle = calculate_angle(hip, knee, ankle)

            if angle > 150:
                stage = "up"
                feedback = "Stand Straight"

            elif angle < 100 and stage == "up":
                stage = "down"
                counter += 1
                feedback = "Good Rep"

            elif 100 <= angle <= 140:
                feedback = "Go Lower"

            if counter < 5:
                suggestion = "Warm up more"
            elif counter < 15:
                suggestion = "Good workout"
            else:
                suggestion = "Increase intensity"

            if counter < 5:
                habit_msg = "You might skip workouts"
                schedule = "Do light workout tomorrow"
            elif counter < 15:
                habit_msg = "Good effort"
                schedule = "Continue same routine"
            else:
                habit_msg = "Excellent consistency"
                schedule = "Increase intensity tomorrow"

            if angle > 150:
                form_score = 10
            elif angle > 120:
                form_score = 7
            else:
                form_score = 5

            score = counter * form_score
            performance_history.append(score)

            if feedback != prev_feedback and feedback != "":
                speak(feedback)
                prev_feedback = feedback

        except:
            score = counter * 10

        if len(performance_history) > 10:
            avg_score = sum(performance_history[-10:]) / 10
        else:
            avg_score = score

        cv2.putText(image, f'Reps: {counter}',
                    (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0,255,0), 2)

        cv2.putText(image, f'Feedback: {feedback}',
                    (10, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0,255,255), 2)

        cv2.putText(image, f'Score: {score}',
                    (10, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255,0,0), 2)

        cv2.putText(image, f'Avg Score: {int(avg_score)}',
                    (10, 160),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255,255,255), 2)

        cv2.putText(image, f'Suggestion: {suggestion}',
                    (10, 200),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (255,255,0), 2)

        cv2.putText(image, f'Habit: {habit_msg}',
                    (10, 240),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (255,255,255), 2)

        cv2.putText(image, f'Next Plan: {schedule}',
                    (10, 280),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0,255,255), 2)

        cv2.putText(image, f'Angle: {int(angle)}',
                    (400, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255,255,255), 2)

        cv2.imshow('AI Fitness Assistant', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()