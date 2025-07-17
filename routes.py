from main import app
from flask import render_template

#rotas
@app.route("/")
def home():
    return render_template ("homepage.html")

@app.route("/blog")
def blog():
    return "Esta é a página do blog."