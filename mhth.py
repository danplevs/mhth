from flask import Flask, render_template
import json


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        with open("./data/DHT11_l.json") as file:
            temperature, humidity = json.load(file).values()
        return render_template("index.html", temperature=temperature, humidity=humidity)

    return app
