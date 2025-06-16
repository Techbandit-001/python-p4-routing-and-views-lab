#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# 1. Base route
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# 2. Print a string
@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

# 3. Count to a number
@app.route('/count/<int:param>')
def count(param):
    numbers = ""
    for i in range(param):
        numbers += f"{i}\n"
    return numbers

# 4. Do math operation
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)

