from flaskext.mysql import MySQL
import flask
import json
from flask import Flask, request, jsonify, make_response
import logging
from logging.handlers import RotatingFileHandler
import time

#Create an object of Flask type
app = Flask(__name__)

#Getting db credentials from a json file so as to hide the details
with open('db_credentials.json') as cred_data:
    info = json.load(cred_data)
    app.config['MYSQL_DATABASE_USER'] = info['MYSQL_DATABASE_USER']
    app.config['MYSQL_DATABASE_PASSWORD'] = info['MYSQL_DATABASE_PASSWORD']
    app.config['MYSQL_DATABASE_DB'] = info['MYSQL_DATABASE_DB']
    app.config['MYSQL_DATABASE_HOST'] = info['MYSQL_DATABASE_HOST']

#Create an object of MySQL
mysql = MySQL(app)

#Landing Page
@app.route('/')
def index():
    app.logger.info(time.strftime('%X %x %Z')+': User entered home page ')
    return ("WELCOME TO BASIC FLASK CRUD APP")

#Show all entries using GET method page
@app.route('/show_all/', methods=['GET'])
def show_all():
    app.logger.info(time.strftime('%X %x %Z')+': User is viewing all data')
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM example""")
    rv = cur.fetchall()
    all_data = {}
    for row in rv:
        all_data[row[0]]=[row[1], row[2]]
    return str(all_data)

@app.route('/reset/', methods=['PUT'])
def reset():
    data = request.get_json()
    reset_status = data["reset_status"]
    app.logger.info(time.strftime('%X %x %Z')+': User is resetting data')
    if reset_status == "Yes":
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("""DROP TABLE example""")
        cur.execute(""" CREATE TABLE example ( id int(11) NOT NULL AUTO_INCREMENT, username varchar(50) NOT NULL, password varchar(50) NOT NULL, PRIMARY KEY (`id`) )""")
        conn.commit()
        return ("Table Reset Complete")
    return("Unable to reset table")



#Insert Single Entry page using POST method page
@app.route('/insert/', methods=['POST'])
def insert_one():
    app.logger.info(time.strftime('%X %x %Z')+': User is inserting new data')
    data = request.get_json()
    try:
        username = data["username"]
        password = data["password"]
    except:
        return str("Insufficient data entered for insertion into DB")
    conn = mysql.connect()
    cur = conn.cursor()
    sql = "INSERT INTO example (username, password) VALUES (%s, %s)"
    val = (username, password)
    cur.execute(sql, val)
    conn.commit()
    return str("INSERTED DETAILS OF USER- "+ username)

#Delete Single Entry using DELETE method page
@app.route('/delete/', methods=['DELETE'])
def delete_one():
    app.logger.info(time.strftime('%X %x %Z')+': User is deleting an entry')
    data = request.get_json()
    try:
        id = data["id"]
    except:
        return str("Insufficient data entered for deletion")
    conn = mysql.connect()
    cur = conn.cursor()
    sql = "SELECT COUNT(*) from example where id = %s"
    val = (id)
    count = cur.execute(sql, val)
    count_var = cur.fetchone()[0]
    if count_var == 0:
        return str("No entry available for the particular id")

    sql = "DELETE FROM example WHERE id= %s "
    val = (id)
    cur.execute(sql, val)
    conn.commit()
    return str("DELETED USER, WHERE ID = "+str(id))


#Update Single Entry using PUT method page
@app.route('/update/', methods=['PUT'])
def update_one():
    app.logger.info(time.strftime('%X %x %Z')+': User is updating an entry')
    data = request.get_json()
    try:
        id = data["id"]
        username = data["username"]
        password = data["password"]
    except:
        return str("Insufficient data entered for updating db entry")

    conn = mysql.connect()
    cur = conn.cursor()
    sql = "SELECT COUNT(*) from example where id = %s"
    val = (id)
    count = cur.execute(sql, val)
    count_var = cur.fetchone()[0]
    if count_var == 0:
        return str("No entry available for the particular id")
    sql = "UPDATE example SET username = %s, password = %s  WHERE id = %s;"
    val = (username,password,id)
    cur.execute(sql, val)
    conn.commit()
    return str("UPDATED ID "+str(id)+" with user "+username)

#Running the flask app using main call
if __name__ == '__main__':
    handler = RotatingFileHandler('logging_file.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True)
