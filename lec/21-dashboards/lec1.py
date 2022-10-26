# Today: dashboards with dynamically generated PNG/SVG plots
import flask
import matplotlib.pyplot as plt
import pandas as pd
import io # input/output (StringIO is a fake text file, BytesIO is a ...)

app = flask.Flask("lec 1 dashboard")

@app.route("/")
def home():
    return """
    <html>
    <body bgcolor=lightblue>
    
    <h3>Example 1: PNG (Cumulative Distribution Function)</h3>
    <img src="plot1.png">
    
    <h3>Example 2: SVG (Histogram)</h3>
    <img src="plot2.svg">
    </body>
    </html>"""

temperatures = [81,70,85,82]

@app.route("/upload", methods=["POST"])
def upload():
    s = str(flask.request.get_data(), "utf-8")
    for num in s.split(","):
        temperatures.append(float(num))
    return f"you now have {len(temperatures)} temperatures\n"


# @app.route("/upload")
# def upload():
#     for t in flask.request.args["temps"].split(","):
#         temperatures.append(float(t))
#     return f"you now have {len(temperatures)} temperatures"

@app.route("/plot1.png")
def plot1():
    # create the plot
    fig, ax = plt.subplots(figsize=(3,2))
    s = pd.Series(sorted(temperatures))
    rev = pd.Series((s.index+1) / len(s) * 100, index=s.values)
    rev.plot.line(ax=ax, ylim=0, drawstyle="steps-post")
    ax.set_xlabel("Temperature")
    ax.set_ylabel("% Temps <=")
    plt.tight_layout()
    
    # send it back
    f = io.BytesIO() # FAKE FILE
    fig.savefig(f)
    plt.close() # just closes the most recent fig
    return flask.Response(f.getvalue(),
                          headers={"Content-Type": "image/png"})

@app.route("/plot2.svg")
def plot2():
    # create the plot
    fig, ax = plt.subplots(figsize=(3,2))
    pd.Series(temperatures).hist(ax=ax, bins=100)
    ax.set_ylabel("Temperature")
    plt.tight_layout()
    
    # send it back
    f = io.StringIO() # FAKE TEXT FILE
    fig.savefig(f, format="svg")
    plt.close() # just closes the most recent fig
    return flask.Response(f.getvalue(),
                          headers={"Content-Type": "image/svg+xml"})

app.run("0.0.0.0", debug=True, threaded=False)