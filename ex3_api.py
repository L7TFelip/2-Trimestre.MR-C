from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/saudacao")
def saudacao():
    return "Seja bem-vindo à minha API!"

@app.route("/data")
def data():
    return f"Data de hoje: {date.today()}"

if __name__ == "__main__":
    app.run(debug=True)

print("Mr - C")