from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(
            host="db",  # Docker container name or network alias
            user="root",
            password="password",
            database="mydb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello from MySQL via Flask and Gunicorn!'")
        result = cursor.fetchone()
        return render_template('index.html', message=result[0])
    except Exception as e:
        return f"DB error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

