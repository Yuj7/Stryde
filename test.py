from flask import Flask, render_template, request, redirect, url_for
import venue_search

app = Flask(__name__)


@app.route("/")
def title():
    return render_template("title.html")


@app.route('/index_button')
def index():
    return render_template("index.html")


@app.route('/register_button')
def register():
    return render_template("register.html")

freq = ""

d = ""

name, store, cit = "", "", ""
ran = False

@app.route('/search_button', methods=["GET", "POST"])
def search():
    if request.method == "POST":
        freq = request.form["searched"]
        names, stores, citi = venue_search.get_stores(freq)
        ran = True
        return home()
    else:
        return render_template("search.html")


# BUTTONS FOR DIFFERENT VENUES' HEATMAP

@app.route('/home_button')
def home():
    if ran:
        d = names
        city = cit
    else:
        d, nothing, city = venue_search.get_stores(freq)
    return render_template("home.html", d=d, city=city)

if ran:
    stores = store
    names = name

@app.route("/heatmap_button0")
def heatmap():
    if ran:
        all_days = stores[0:7]
    else:
        all_days = venue_search.get_stores(freq)[1][0:7]
    return render_template("graph.html", all_days=all_days)


@app.route("/heatmap_button1")
def heatmap1():
    if ran:
        all_days = stores[7:14]
    else:
        all_days = venue_search.get_stores(freq)[1][7:14]

    return render_template("graph.html", all_days=all_days)

if ran:
    stores = store

@app.route("/heatmap_button2")
def heatmap2():
    all_days = stores[14:21]
    return render_template("graph.html", all_days=all_days)


@app.route("/heatmap_button3")
def heatmap3():
    all_days = stores[21:28]
    return render_template("graph.html", all_days=all_days)


@app.route("/heatmap_button4")
def heatmap4():
    all_days = stores[28:35]
    return render_template("graph.html", all_days=all_days)


@app.route("/heatmap_button5")
def heatmap5():
    all_days = stores[35:42]
    return render_template("graph.html", all_days=all_days)


@app.route("/heatmap_button6")
def heatmap6():
    all_days = stores[42:49]
    return render_template("graph.html", all_days=all_days)


@app.route("/heatmap_button7")
def heatmap7():
    all_days = stores[49:56]
    return render_template("graph.html", all_days=all_days)


@app.route("/heatmap_button8")
def heatmap8():
    all_days = stores[56:63]
    return render_template("graph.html", all_days=all_days)


@app.route("/heatmap_button9")
def heatmap9():
    all_days = stores[63:70]
    return render_template("graph.html", all_days=all_days)


@app.route("/heatmap_button10")
def heatmap10():
    all_days = stores[70:79]
    return render_template("graph.html", all_days=all_days)


@app.route("/heatmap_button11")
def heatmap11():
    all_days = stores[79:86]
    return render_template("graph.html", all_days=all_days)


if __name__ == '__main__':
    port = 1120  # the custom port you want
    app.run(host='127.0.0.1', port=port)