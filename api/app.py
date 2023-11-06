from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


@app.route("/github_form")
def github_form():
    return render_template("github_username.html")


@app.route("/hello_github_user", methods=["POST"])
def hello_github_user():
    username = request.form.get("username")
    return render_template("hello_github_user.html", username=username)


@app.route("/github_repositories/<username>")
def get_github_repositories(username):
    response = requests.get(f"https://api.github.com/users/Lianyic/repos")
    if response.status_code == 200:
        repositories = response.json()
        return render_template("github_repositories.html", repositories=repositories)
    else:
        return "Failed to fetch GitHub repositories"


def process_query(query):
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth"
    if query == "asteroids":
        return "Unknown"


@app.route("/query/<q>")
def query(q):
    result = process_query(q)
    return result
