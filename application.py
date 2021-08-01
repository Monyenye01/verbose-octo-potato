import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import sqlite3

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    print("yes")
    return render_template("index.html")

@app.route("/cakes")
def cakes():
    print("yes")
    return render_template("cakes.html")
