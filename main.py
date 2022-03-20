
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")
print("homepage rodando")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/posts/<poste1>")
def posts(poste1):
    return render_template("posts.html", poste1=poste1)

@app.route("/contatos/<contato1>")
def posts(contato1):
    return render_template("contatos.html", contato1=contato1)

if __name__ =="__main__":
    app.run(debug=True)


