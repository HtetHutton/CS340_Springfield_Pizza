from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import database.db_connector as db
import os

app = Flask(__name__)


mysql = MySQL(app)

db_connection = db.connect_to_database()

# Routes

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/Customers')
def Customers():
    return render_template('Customers.html')


@app.route('/Employees')
def Employees():
    return render_template('Employees.html')

@app.route('/Pizzas')
def Pizzas():
    return render_template('Pizzas.html')


@app.route('/Orders')
def Orders():
    return render_template('Orders.html')

# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=6757, debug=True) 