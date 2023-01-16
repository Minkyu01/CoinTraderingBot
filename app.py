from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/') #나중에 URL coinback으로 수정
def coin():
    return render_template("coinbacktest.html")