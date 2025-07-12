from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    # Connect to DB to show DB is working
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database="appdb",
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        conn.close()
        return "Connected to DB and Hello from Flask!"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

