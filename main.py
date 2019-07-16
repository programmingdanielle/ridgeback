from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def test():
    question = request.form["question"]
    question2 = request.form["question2"]
    question3 = request.form["question3"]
    answer = answer_test(question, question2, question3)
    return answer

def answer_test(q1, q2, q3):
    questions = [q1, q2, q3]
    firedrake = 0
    waterdrake = 0
    earthdrake = 0
    for question in questions:
        if question == "a":
            firedrake += 1
        if question == "b":
            waterdrake += 1
        if question == "c":
            earthdrake += 1
    if firedrake > waterdrake and firedrake > earthdrake:
        return "You are a firedrake."
    if waterdrake > firedrake and waterdrake > earthdrake:
        return "You are a waterdrake."
    if earthdrake > firedrake and earthdrake > waterdrake:
        return "You are an earthdrake."
    else:
        return "You're a tricky one, aren't you? Visit the Egg Shop at another time, and we'll see what we can do for you."



if __name__ == "__main__":
    app.run()