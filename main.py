import os
import pymysql
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"
db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "flask_user"),
    "password": os.getenv("DB_PASS", "flask_pass"),
    "database": os.getenv("DB_NAME", "flask_db"),
    "port": int(os.getenv("DB_PORT", 3306))
}

def get_connection():
    return pymysql.connect(**db_config)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (usuario, password))
            user = cursor.fetchone()
            cursor.close()
            conn.close()

            if user:
                flash("✅ Inicio de sesión correcto", "success")
                return redirect(url_for('dashboard', username=usuario))
            else:
                flash("❌ Usuario o contraseña incorrectos", "danger")
        except Exception as e:
            flash(f"❌ Error conectando a DB: {e}", "danger")

    return render_template('login.html')

@app.route('/dashboard/<username>')
def dashboard(username):
    return f"<h1>Bienvenido, {username}!</h1><p>Has iniciado sesión correctamente.</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
