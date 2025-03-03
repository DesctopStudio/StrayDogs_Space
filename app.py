from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

if __name__ == '__main__':
    app.run()
