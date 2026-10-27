from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    student_name = "Lia"
    program = "Computation Arts" 

    return render_template("index.html", name = student_name, degree=program)

app.run(debug=True)