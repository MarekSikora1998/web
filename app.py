from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# PostgreSQL connection details
conn = psycopg2.connect(
    host="10.132.208.77",
    database="postgres",
    user="postgres",
    password="temp"
)

@app.route('/')
def show_data():
    # Fetch data from PostgreSQL
    cur = conn.cursor()
    cur.execute("SELECT * FROM score.monitoring")
    data = cur.fetchall()

    # Render data in a table using a template
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()

