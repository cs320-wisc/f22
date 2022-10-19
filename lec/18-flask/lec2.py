import flask, time   # pip3 install flask

app = flask.Flask("my application")

# TEMPLATING (a kind of dynamic)
@app.route("/time.html")
def clock():
    with open("time.html") as f:
        mystring = f.read()
    mystring = mystring.replace("REPLACE_ME", str(time.time()))
    print("DEBUG:", mystring)
    return mystring

# DYNAMIC
@app.route("/ha.html")
def laugh():
    s = "haha " * 1000
    return s

# STATIC
@app.route("/")
def home():
    with open("index.html") as f:
        html = f.read()
        
    return html

if __name__ == "__main__":
    print("BEFORE")
    app.run(host="0.0.0.0", debug=True, threaded=False)
    print("AFTER")

# app.run never returns, so don't define functions
# after this (the def lines will never be reached)
