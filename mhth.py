from flask import Flask, render_template
from sensors import get_DHT11


app = Flask(__name__)

@app.route("/")
def index():
    temperature, humidity = get_DHT11().values()
    return render_template("index.html", temperature=temperature, humidity=humidity)
