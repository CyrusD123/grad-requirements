from app import application, engine, session, metadata
from flask import Flask, jsonify, request, render_template
from sqlalchemy import Table

@application.route('/')
def hello():
    return "Hello World!"