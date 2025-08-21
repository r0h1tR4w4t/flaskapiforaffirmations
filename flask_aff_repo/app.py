from flask import Flask, jsonify , redirect
import random

affirmations = [
    "You are capable of amazing things.",
    "Believe in yourself.",
    "Every day is a new opportunity.",
    "You are worthy of love and respect.",
    "Stay positive and strong.",
]

app = Flask(__name__)

@app.route('/affirmation', methods=['GET'])
def get_affirmation():
    affirmation = random.choice(affirmations)
    return jsonify({"affirmation": affirmation})

@app.route('/')
def home():
    return redirect("/affirmation")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
