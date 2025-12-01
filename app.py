from flask import Flask
from urls import news_bp
from admin import admin_bp


app = Flask(__name__)
app.config['SECRET_KEY'] = 'news'

app.register_blueprint(news_bp)
app.register_blueprint(admin_bp)

if __name__=="__main__":
    app.run(debug=True)