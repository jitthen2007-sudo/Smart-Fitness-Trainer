from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Fitness Backend Running"}


@app.get("/recommend")
def recommend(goal: str):
    if goal == "lose":
        return {"plan": "Cardio + HIIT", "challenge": "Run 10 mins daily"}
    elif goal == "gain":
        return {"plan": "Weight training", "challenge": "Do 20 pushups daily"}
    else:
        return {"plan": "Balanced workout", "challenge": "Stay active daily"}


@app.get("/admin")
def admin():
    return {
        "total_users": 1,
        "total_workouts": 20,
        "avg_score": 85,
        "status": "System running"
    }