import flask, time

app = flask.Flask("my application")

# TEMPLATE (kind of dynamic)
@app.route("/time.html")
def clock():
    with open("time.html") as f:
        s = f.read()
    s = s.replace("REPLACE_ME", str(time.time()))
    print("DEBUG:", s)
    return s

# DYNAMIC
@app.route("/ha.html")
def laugh():
    return "hahaha"*1000

# STATIC
@app.route("/")
def home():
    with open("index.html") as f:
        html = f.read()
        
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, threaded=False)

# app.run never returns, so don't define functions
# after this (the def lines will never be reached)
