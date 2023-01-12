from flask import Flask, render_template, request
app = Flask(__name__)
seq = [2, 3, 4, 5, 6]


@app.route("/", methods=["GET", "POST"])  # default: GET
def show_form():
    if request.method == "POST":
        if request.values["send"] == "Send":
            return render_template("index.html", name=request.values["user"],
                                   seq=seq)
    else:
        return render_template("index.html", name="")


@app.route("/param")
def get_param():
    return request.args.get("param1")


@app.route("/js")
def show_js():
    return render_template("js.html")


@app.route("/css")
def show_css():
    return render_template("css.html")


@app.route("/extend")
def show_extendhtml():
    return render_template("extend.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="77", debug=True)