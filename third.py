from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<title>/<name>/<age>')
def root(title, name, age) -> 'html':
    return render_template("index.html", title=title, name=name, age=int(age),)

if __name__ == '__main__':
    app.run(debug=True)