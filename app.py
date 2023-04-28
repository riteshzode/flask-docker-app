
from flask import Flask, render_template
import requests
import json
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("meme_index.html")


if __name__ == "__main__":
    app.run(debug=True)