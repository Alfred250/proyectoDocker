import os
import pymysql
from flask import Flask, render_template

app = Flask(__name__)

db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "flask_user"),
    "password": os.getenv("DB_PASS", "flask_pass"),
    "database": os.getenv("DB_NAME", "flask_db"),
    "port": int(os.getenv("DB_PORT", 3306))
}

def get_connection():
    return pymysql.connect(**db_config)

@app.route('/')
def main():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT NOW();")   
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('login.html', name="Login", time=result[0])
    except Exception as e:
        return f"❌ Error conectando a DB: {e}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
