from flask import Flask, render_template
import json


app = Flask(__name__)

@app.route("/")
def index():
    with open("./data/DHT11_l.json") as file:
        temperature, humidity = json.load(file).values()
    return render_template("index.html", temperature=temperature, humidity=humidity)

if __name__ == "__main__":
    app.run()
