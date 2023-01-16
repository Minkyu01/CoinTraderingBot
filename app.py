from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/coinback')
def coin():
    return render_template("coinbacktest.html")