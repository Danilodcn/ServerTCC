from flask import Flask, jsonify, render_template

from os import getpid
from pprint import pprint
from time import sleep
from random import random
from multiprocessing import Pool


def func(n):
    n = int(n)
    print(f"Processo {n}")
    sleep(random() / 10)
    return {n + 1: getpid()}


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def nome():
        return render_template("home.html")

    @app.route("/n/<int:n>")
    def home(n):
        workers = Pool(3)
        response = workers.map(func, range(n))
        return jsonify({"nome": response})

    return app


if __name__ == "__main__":
    app = create_app()
    app.debug = True
    app.run()