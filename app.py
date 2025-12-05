from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def advice():
    data = requests.get("https://api.adviceslip.com/advice").json()
    return f"<h2>{data['slip']['advice']}</h2>"

if __name__ == "__main__":
    app.run(debug=True)
