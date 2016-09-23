from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def page_index():
    return render_template("base_article.html")

if __name__ == '__main__':
    app.run()