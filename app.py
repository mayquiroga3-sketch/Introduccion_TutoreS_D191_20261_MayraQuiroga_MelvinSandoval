from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "clave_secreta"

def get_db():
    return sqlite3.connect("database.db")

@app.route("/")
def inicio():
    return render_template("login.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        rol = request.form["rol"]
        db = get_db()
        db.execute("INSERT INTO usuarios (nombre, rol) VALUES (?,?)", (nombre, rol))
        db.commit()
        return redirect("/")
    return render_template("registro.html")

@app.route("/reservar", methods=["GET", "POST"])
def reservar():
    if request.method == "POST":
        fecha = request.form["fecha"]
        db = get_db()
        db.execute("INSERT INTO tutorias (fecha) VALUES (?)", (fecha,))
        db.commit()
    return render_template("reservar.html")

app.run(debug=True)
