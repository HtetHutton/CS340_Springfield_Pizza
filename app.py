from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_vasquem2'
app.config['MYSQL_PASSWORD'] = '9610' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_vasquem2'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)


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