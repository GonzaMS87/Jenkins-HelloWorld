from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    return render_template("index.html", hora_actual=hora_actual)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

