from os import name
from flask import Flask, render_template # type: ignore
from helpers import get_news

app = Flask(__name__)
app.secret_key = "TheNews"

@app.route("/")
def index():
    response = get_news()
    return render_template("index.html", json = response)


if __name__=="__main__":
    app.run(debug=True)