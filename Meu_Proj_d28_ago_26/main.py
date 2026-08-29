from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("imc.html")


@app.route("/resultado", methods=["POST"])
def resultado():
    peso = float(request.form["peso"])
    altura = float(request.form["altura"])

    altura_metros = altura / 100
    altura_quadrada = altura_metros*altura_metros
    imc = peso / altura_quadrada

    if imc < 18.5:
        fisico = "Baixo"
    elif imc < 25:
        fisico = "Normal"
    elif imc < 30:
        fisico = "Sobrepeso"
    else:
        fisico = "Obeso"

    return render_template(
    "imc.html",
    peso=peso,
    altura=altura,
    imc=round(imc, 2),
    fisico=fisico
    )


if __name__ == "__main__":
    app.run(debug=True)