# Main program code
import os
import openai
from flask import Flask, jsonify, redirect, render_template, request, url_for
import mysql.connector

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

#TODO: change these
#connection = mysql.connector.connect(
    #host="HOST",
    #user="doadmin",
    #password="PW",
    #database="defaultdb",
    #port=0000
#)


#db_cursor = connection.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scout', methods=['GET', 'POST'])
def scout():
    if request.method == 'POST':
        # TODO: Handle form submission or other POST logic here
        return jsonify(request.form)
    else:
        return render_template('scoutLanding.html')

@app.route('/analyze')
def analyze():
    return render_template('analyzeLanding.html')







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)