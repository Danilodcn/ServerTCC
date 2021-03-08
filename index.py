from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")
def home():
    files = open("Home.html")
    x = files.read()
    return "<div>" + x + "</div>"


@app.route("/segunda")
def segunda():
    return """
    <h1>Segunda</h1>
    <a href='/'> Home </a>
    """