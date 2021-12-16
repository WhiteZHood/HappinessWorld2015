from flask import Flask, send_file, render_template
import seaborn as sns
import pandas as pd
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html", links=links, image=None)

@app.route('/download', methods=['GET'])
def download_data():
    return send_file("data/2015.csv", as_attachment=True)

links = {"2015 year data" : "/download",
         "2015: Happiness vs Spheres" : "/happiness_life_spheres",
         "2015: Happiness in Regions" : "happiness_regions",
         "2015: Spheres in Regions" : "life_spheres_regions"}

def render_index (image = None):
    return render_template("index.html", links=links, image = (image, image), code=time.time())
