import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_ID = "gemini-2.5-flash"


def generate_workout_gemini(name, age, weight, goal, intensity):
    """Generate a workout plan using Gemini AI"""
    
    prompt = f"""
    Create a weekly workout plan for:

    Name: {name}
    Age: {age}
    Weight: {weight} kg
    Goal: {goal}
    Workout Intensity: {intensity}

    The workout should include:
    - 5–6 day split
    - exercises
    - sets and reps
    - short explanation
    """

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )

    return response.text


def generate_nutrition_tip_with_flash(goal):
    """Generate a short nutrition tip"""

    prompt = f"""
    You are an expert sports nutritionist.
    Give ONE short actionable nutrition tip (max 2 sentences)
    for someone whose fitness goal is: {goal}.
    """

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )

    return response.text


def update_workout_plan(old_plan, feedback):
    """Update the workout plan based on user feedback"""

    prompt = f"""
    This is the current workout plan:

    {old_plan}

    The user gave this feedback:
    {feedback}

    Modify the workout plan accordingly.
    """

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )

    return response.text