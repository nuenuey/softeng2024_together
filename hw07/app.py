from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dodo")
def dodo():
    return render_template('dodo.html')

@app.route("/soonday")
def soonday():
    return render_template('soonday.html')

@app.route("/so_ba")
def so_ba():
    return render_template('so_ba.html')

@app.route("/flower")
def flower():
    return render_template('flower.html')

@app.route("/king")
def king():
    return render_template('king.html')

@app.route("/onedanggo")
def onedanggo():
    return render_template('onedanggo.html')

if __name__ == "__main__":
    app.run(debug=True)