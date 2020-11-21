from flask import Flask, jsonify, request, render_template
import os
import psycopg2

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()