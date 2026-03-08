"""
FitBuddy - AI-Powered Fitness Planner
Backend built with Flask + SQLite + Google Gemini AI
"""

import os
import json
import logging
import sqlite3
from flask import Flask, request, jsonify, render_template

# ---------------- Logging ----------------

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fitbuddy")

# ---------------- App Setup ----------------

app = Flask(__name__, template_folder="templates", static_folder="static")

DB_PATH = "fitbuddy.db"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

# ---------------- Database ----------------


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:

        conn.execute(
            """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            weight REAL,
            height REAL,
            goal TEXT,
            intensity TEXT
        )
        """
        )

        conn.execute(
            """
        CREATE TABLE IF NOT EXISTS workout_plans(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            plan_json TEXT,
            nutrition_tip TEXT
        )
        """
        )

# ---------------- Gemini / Mock AI ----------------


def generate_mock_plan():

    plan = {
        "days": [
            {
                "day": "Day 1",
                "focus": "Full Body",
                "exercises": ["Push ups", "Squats", "Plank"],
            },
            {
                "day": "Day 2",
                "focus": "Cardio",
                "exercises": ["Jogging", "Jump Rope"],
            },
        ],
        "summary": "Simple starter fitness plan",
    }

    return plan


def generate_mock_tip():

    return {
        "icon": "💪",
        "tip": "Eat protein after workouts and stay hydrated.",
    }

# ---------------- Routes ----------------


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/generate-plan", methods=["POST"])
def generate_plan():

    data = request.get_json(silent=True) or request.form.to_dict() or {}

    logger.info("Received data: %s", data)

    name = data.get("name", "").strip()
    age = int(data.get("age", 0))
    weight = float(data.get("weight", 0))
    height = data.get("height")
    goal = data.get("goal", "").lower()
    intensity = data.get("intensity", "").lower()

    user = {
        "name": name,
        "age": age,
        "weight": weight,
        "height": height,
        "goal": goal,
        "intensity": intensity,
    }

    # generate plan

    plan_data = generate_mock_plan()

    tip_data = generate_mock_tip()

    # save user

    with get_db() as conn:

        cursor = conn.execute(
            """
            INSERT INTO users(name,age,weight,height,goal,intensity)
            VALUES(?,?,?,?,?,?)
            """,
            (name, age, weight, height, goal, intensity),
        )

        user_id = cursor.lastrowid

        conn.execute(
            """
            INSERT INTO workout_plans(user_id,plan_json,nutrition_tip)
            VALUES(?,?,?)
            """,
            (user_id, json.dumps(plan_data), json.dumps(tip_data)),
        )

    # return jsonify(
    #     {
    #         "success": True,
    #         "user_id": user_id,
    #         "plan": plan_data,
    #         "nutrition_tip": tip_data,
    #     }
    # )
    return render_template(
    "result.html",
    plan=plan_data,
    tip=tip_data,
    user_name=name
)


@app.route("/view-all-users")
def view_all_users():

    with get_db() as conn:

        users = conn.execute("SELECT * FROM users").fetchall()

        users = [dict(u) for u in users]

    return render_template("all_users.html", users=users)

# ---------------- Error Handlers ----------------


@app.errorhandler(404)
def not_found(e):

    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def server_error(e):

    logger.error("Server error: %s", str(e))

    return jsonify({"error": "Internal server error"}), 500

# ---------------- Main ----------------


if __name__ == "__main__":

    init_db()

    print("FitBuddy running at http://127.0.0.1:5000")

    app.run(host="0.0.0.0", port=5000)