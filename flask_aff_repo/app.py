import os
from flask import Flask, jsonify, redirect
import random

app = Flask(__name__)

affirmations = [
    "You are capable of amazing things.",
    "Believe in yourself.",
    "Every day is a new opportunity.",
    "You are worthy of love and respect.",
    "Stay positive and strong.",
]

@app.route("/affirmation")
def get_affirmation():
    affirmation = random.choice(affirmations)
    return jsonify({"affirmation": affirmation})

@app.route("/")
def index():
    return redirect("/affirmation")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway sets PORT dynamically
    app.run(host="0.0.0.0", port=port, debug=True)

