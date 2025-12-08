from flask import Flask, render_template, request # type: ignore
from helpers import NEWS

d = NEWS()
app = Flask(__name__)
app.secret_key = "TheNews"



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        response = d.get_news()
        return render_template("index.html", json = response)
    else:
        response = d.news_q(request.form.get("q")) 
        return render_template("index.html", json = response)


@app.route("/about")
def about():
    return render_template("about.html")

     
if __name__=="__main__":
    app.run(debug=True)