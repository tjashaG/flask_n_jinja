from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    users = ["Tom", "Dick", "Harry"]

    users_info = {
        "Tom": "Engineer",
        "Mike": "Teacher",
        "John": "Lawyer",
        "Frank": "Hobo"
    }

    return render_template("index.html", users=users, users_info=users_info)

@app.route("/about")
def about():
    my_name = "Tjasa Guzej"
    my_age = 35

    return render_template("about.html", my_name=my_name, my_age=my_age)

if __name__ == "__main__":
    app.run(debug=True)
