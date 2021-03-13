from flask import Flask, request, jsonify
import calculos
from random import random

app = Flask(__name__)

print(__name__)

@app.route("/")
def home():
    files = open("templates/Home.html")
    x = files.read()
    return "<div>" + x + "</div>"


@app.route("/segunda", methods=["GET"])
def segunda():
    return """
    <h1>Segunda</h1>
    <a href='/'> Home </a>
    """

@app.route("/calculo/", methods=["GET"])
def rota():
    retorno = {"status": "sucess"}
    if request.method == "GET":
        try:
            n = request.args.get("n")
            b = True if request.args.get("b") == "True" else False
            calc = calculos.sort([random() for i in range(int(n))], b)
            if request.args.get("tipo"):
                retorno[request.args.get("tipo")] = calc[request.args.get("tipo")]
            else:
                retorno["Calculo"] =  calc
        except Exception as e:
            retorno = {"status": "Erro : " + str(e)}
        

    return jsonify(retorno)


def route_calculo():
    retorno = {"status": "sucess"}
    if request.method == "GET":
        try:
            n = request.args.get("n")
            b = True if request.args.get("b") == "True" else False
            retorno["Calculo"] =  calculos.sort([random() for i in range(int(n))], b)
        except Exception as e:
            retorno = {"status": "Erro : " + str(e)}
        

    return jsonify(retorno)
