
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bem-vindo"

@app.route("/curso")
def curso():
    return "Nome do seu curso"

@app.route("/escola")
def escola():
    return "Nome da sua escola"

if __name__ == "__main__":
    app.run(debug=True)

print("Mr - C")