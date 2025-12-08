from dotenv import load_dotenv # type: ignore
import requests # type: ignore
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

class NEWS():
    def get_news(self) -> list:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
        response = requests.get(url)
        if not response.status_code == 200:
            raise Exception("Error")
        return response.json()["articles"]


    def news_q(self, q) -> list:
        url = f"https://newsapi.org/v2/everything?q={q}&sortBy=publishedAt&apiKey={API_KEY}"
        response = requests.get(url)
        if not response.status_code == 200:
            raise Exception("Error")
        return response.json()["articles"]

if __name__=="__main__":
    NEWS()
