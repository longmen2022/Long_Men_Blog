from flask import Flask, render_template
import requests

#USE YOUR OWN npoint LINK! OTHERWISE IT WILL NOT WORK 👇
posts = requests.get("https://api.npoint.io/dd8463a897d2f65407d7").json()

app = Flask(__name__)


# @app.route('/')
# def get_all_posts():
#     return render_template("home.html", all_posts=posts)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", all_posts=posts)



@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/experience")
def experience():
    return render_template("experience.html")

if __name__ == "__main__":
    app.run(debug=True)