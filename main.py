from flask import Flask, render_template, request
from translate import get

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def process():
    a = ''
    if request.method == "POST":
        text = request.form.get('inp')
        lang = request.form.get('lan')
        a = get(text, lang)
    return render_template('index.html', name=a)


if __name__ == "__main__":
    app.run(debug=True)
