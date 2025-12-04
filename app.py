from flask import Flask
from datetime import timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = 'news'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1) # session only store for 1 day 
app.config['DEBUG'] = True



if __name__=="__main__":
    app.run(debug=True)