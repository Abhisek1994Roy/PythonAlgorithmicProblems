from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'sql12258002'
app.config['MYSQL_DATABASE_PASSWORD'] = 'wyNLnPRq2V'
app.config['MYSQL_DATABASE_DB'] = 'sql12258002'
app.config['MYSQL_DATABASE_HOST'] = 'sql3.freemysqlhosting.net'
mysql.init_app(app)
