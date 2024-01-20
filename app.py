from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "index page"  # ブラウザに表示される文字列


if __name__ == "__main__":
    app.run()
