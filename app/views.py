from app import app
import base64
from io import BytesIO
from flask import render_template

from matplotlib.figure import Figure


@app.route("/")
def index():
    return render_template("public/index.html")

@app.route('/matplotlib')
def matplotlib():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save if to a file
    fname = "app/static/img/data/matplotlib.png"
    fig.savefig(fname, format="png")
    # Create file path to file
    data_filepath = "app/static/img/data/matplotlib.png"

    return render_template("public/matplotlib.html", data_filepath=data_filepath)
    # return f"<img src='data:image/png;base64,{data}'/>"


