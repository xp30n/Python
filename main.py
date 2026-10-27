from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/students")
def index():
    students = [
    {"name": "Lia", "program": "Computation Arts"},
    {"name": "Alex", "program": "Computer Science"},
    {"name": "Sam", "program": "Fine Arts"}
    ]

    return render_template("index.html", students=students)

@app.route("/")
def form():
    return render_template("forms.html")

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        username = request.form.get("username", "")

        if username.strip() == "":
            username = "Guest"

        return f"Hello {username}!"

    return "Please submit the form"

app.run(debug=True)