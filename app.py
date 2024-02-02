# coding: utf-8
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")  # テンプレートを表示する


@app.route("/hello")
def hello():
    return "<h1>Hello World!</h1>"  # ブラウザに表示される文字列


@app.route("/user/<user_id>")
def user_id(user_id):  # デコレータで定義した変数と引数を合わせる
    """
    URLによって動的に変更されるページを作成
    """
    return "<h1>Hello {0}!</h1>".format(user_id)


@app.route("/template_inherit")
def template_inherit():
    """
    templates/super.htmlを継承したsub.htmlを表示する
    """
    return render_template("sub.html")


@app.route("/template_jinja/<user_name>")
def template_jinja(user_name):
    """
    templates/jinja.htmlを表示する
    """
    return render_template("jinja.html", user_name=user_name)


@app.errorhandler(404)
def error_404(error):
    """_summary_
    デフォルトのエラー画面でないオリジナルのエラー画面を表示する
    """
    return render_template("error_pages/404.html")


if __name__ == "__main__":
    # app.run()
    # debug modeでブラウザから詳細なエラーが見られる。また，アプリの変更がアプリの再起動なしに反映される。
    app.run(debug=True)
