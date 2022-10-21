# routes: /slow, /never, /robots.txt, /add, /survey
import flask, time

app = flask.Flask("lecture demo")

counts = {}

@app.route("/survey")
def survey():
    major = flask.request.args.get("major", "unkown")
    if not major in counts:
        counts[major] = 0
    counts[major] += 1
    
    return "MAJORS: " + str(counts)

@app.route("/add")
def adder():
    args = dict(flask.request.args)
    try:
        x = float(args["x"])
        y = float(args["y"])
    except KeyError:
        return "please specify x and y"
    return f"{x} + {y} = {x+y}"

@app.route("/never")
def never():
    return "humans only, not bots allowed!"

@app.route("/robots.txt")
def bot_rules():
    return flask.Response("""User-Agent: *
Disallow: /never
""", headers={"Content-Type": "text/plain"})

# GOAL: don't let people visit this more often than once per 3s
last_visit = 0 # TODO: dict of visit times, for each IP

@app.route("/slow")
def slow():
    global last_visit
    print("VISITOR", flask.request.remote_addr)
    if time.time() - last_visit > 3:
        last_visit = time.time()
        return "welcome!"
    else:
        return flask.Response("<b>go away</b>",
                              status=429,
                              headers={"Retry-After": "3"})

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, threaded=True) # threaded=False usually in 320