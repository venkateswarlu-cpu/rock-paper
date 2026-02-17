from flask import Flask, render_template, jsonify

import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play/<user_choice>")
def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "Draw"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You Win 🎉"
    else:
        result = "Computer Wins 😢"

    return jsonify({
        "user": user_choice,
        "computer": computer_choice,
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
