from flaskext.mysql import MySQL
import flask
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'sql12258002'
app.config['MYSQL_DATABASE_PASSWORD'] = 'wyNLnPRq2V'
app.config['MYSQL_DATABASE_DB'] = 'sql12258002'
app.config['MYSQL_DATABASE_HOST'] = 'sql12.freemysqlhosting.net'


mysql = MySQL(app)

@app.route('/')
def index():
    return ("WELCOME TO BASIC FLASK CRUD APP")


@app.route('/show_all/', methods=['GET'])
def show_all():
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM example""")
    rv = cur.fetchall()
    all_data = {}
    for row in rv:
        all_data[row[0]]=row[1]
    return str(all_data)


@app.route('/insert/', methods=['POST'])
def insert_one():
    data = request.get_json()
    id = data["id"]
    text = data["text"]
    conn = mysql.connect()
    cur = conn.cursor()
    sql = "INSERT INTO example (id, data) VALUES (%s, %s)"
    val = (id, text)
    cur.execute(sql, val)
    conn.commit()
    return str("INSERTED NEW ROW AT ID = "+str(id))

@app.route('/delete/', methods=['DELETE'])
def delete_one():
    data = request.get_json()
    id = data["id"]
    conn = mysql.connect()
    cur = conn.cursor()
    sql = "DELETE FROM example WHERE id= %s "
    val = (id)
    cur.execute(sql, val)
    conn.commit()
    return str("DELETED ROW, WHERE ID = "+str(id))




if __name__ == '__main__':
    app.run(debug=True)
