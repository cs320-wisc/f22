# routes: /slow, /never, /robots.txt, /add, /survey
import flask, time

app = flask.Flask("lecture 2 demo")

counts = {}

@app.route("/survey")
def survey():
    arg = dict(flask.request.args)
    major = arg["major"]
    if not major in counts:
        counts[major] = 0
    counts[major] += 1
    return "MAJORS: " + str(counts)

@app.route("/add")
def adder():
    arg = dict(flask.request.args)
    try:
        x = float(arg["x"])
        y = float(arg["y"])
    except KeyError:
        return f"need x and y!"
    print(arg)
    return f"{x}+{y} = {x+y}"

@app.route("/never")
def never():
    return "for humans only (bots not allowed!)"

@app.route("/robots.txt")
def bot_rules():
    return flask.Response("""User-Agent: *
Disallow: /never
""", headers={"Content-Type": "text/plain"})


# TODO: use dict, where key is IP, value is last visit time
last_visit = 0 # seconds since 1970

# GOAL: don't let bots visit it more than once per 3s
@app.route("/slow")
def slow():
    global last_visit
    print("VISITOR:", flask.request.remote_addr)
    
    curr_time = time.time()
    if curr_time - last_visit >= 3:
        last_visit = curr_time
        return "welcome!"
    else:
        return flask.Response("go <b>away!</b>", status=429,
                              headers={"Retry-After": 3})

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, threaded=True)  # generally have threaded=False in 320