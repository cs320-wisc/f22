# Today: dashboard pages with dynamically generated PNG images (for the plots)
import flask
import matplotlib.pyplot as plt
import io # input/output (BytesIO for fake binary file)
          #              (StringIO for fake text file)
import pandas as pd

app = flask.Flask("lec 2 demo")

@app.route("/")
def home():
    return """
    <html>
    <body bgcolor=lightblue>
    <h3>Example 1: PNG (cumulative distribution function)</h3>
    <img src="plot1.png">
    
    <h3>Example 2: SVG (a histogram)</h3>
    <img src="plot2.svg">
    </body>
    </html>
    """

temperatures = [80,85,83,90]

@app.route("/upload", methods=["POST"])
def upload():
    data = str(flask.request.get_data(), "utf-8")
    for value in data.split(","):
        temperatures.append(float(value))
    return f"thanks, you now have {len(temperatures)} records\n"

# @app.route("/upload")
# def upload():
#     print(flask.request.args["temps"]) # query string
#     for value in flask.request.args["temps"].split(","):
#         temperatures.append(float(value))
#     return f"thanks, you now have {len(temperatures)} records"

@app.route("/plot1.png")
def plot1():
    # generate the image
    fig, ax = plt.subplots(figsize=(3,2))
    s = pd.Series(sorted(temperatures))
    rev = pd.Series((s.index+1)/len(s)*100, index=s.values)
    rev.plot.line(ax=ax, ylim=0, drawstyle="steps-post")
    ax.set_xlabel("Temperature")
    ax.set_ylabel("% nums <=")
    plt.tight_layout()
    
    # send image back
    f = io.BytesIO() # fake "file" object
    fig.savefig(f)
    plt.close() # closes most recent fig
    return flask.Response(f.getvalue(),
                          headers={"Content-Type": "image/png"})

@app.route("/plot2.svg")
def plot2():
    # generate the image
    fig, ax = plt.subplots(figsize=(3,2))
    pd.Series(temperatures).hist(ax=ax, bins=100)
    ax.set_ylabel("Temperature")
    plt.tight_layout()
    
    # send image back
    f = io.StringIO() # fake text "file" object
    fig.savefig(f, format="svg")
    plt.close() # closes most recent fig
    return flask.Response(f.getvalue(),
                          headers={"Content-Type": "image/svg+xml"})

app.run("0.0.0.0", debug=True, threaded=False)