from flask import Flask, jsonify, request, render_template
import os
import psycopg2

app = Flask(__name__)

# Connect to database using heroku environment variable DATABASE_URL
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')# Heroku requires SSL

# Create a cursor to execute queries
cursor = conn.cursor()


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
    cursor.close()
    conn.close()