from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route("/")
def home() :
    if "username" in session:
     return render_template("index.html")

@app.route("/a")
def dashbaord() :
   return render_template("dashboard.html")
   


if __name__ == "__main__" :
    app.run(debug=True)

