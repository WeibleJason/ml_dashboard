from app import app
import base64
from io import BytesIO

from matplotlib.figure import Figure


@app.route("/")
def index():
    return "Hello world"

@app.route('/matplotlib')
def matplotlib():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"