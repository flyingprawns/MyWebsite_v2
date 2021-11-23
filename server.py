from flask import Flask, render_template

app = Flask(__name__)


# ------- Flask Code -------- #
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/namecard")
def namecard():
    return render_template("NameCard.html")


if __name__ == "__main__":
    app.run(debug=True)
