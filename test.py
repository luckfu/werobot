#!/alidata1/www-data/WeRoBot/env/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, g
from flaskext.mysql import MySQL

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123123@127.0.0.1/webapp'
#db = SQLAlchemy(app)
#这个测试很变态
#git 不好用啊

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_PORT']=3306
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='123123'
app.config['MYSQL_DATABASE_DB']='webapp'
app.config['MYSQL_DATABASE_CHARSET']='utf8'
mysql = MySQL()
mysql.init_app(app)

mysql = MySQL()
mysql.init_app(app)


@app.before_request
def connect_db():
    g.db = Connection(config.DB_HOST,
                      config.DB_NAME,
                      config.DB_USER,
                      config.DB_PASSWD)

@app.after_request
def close_connection(response):
    g.db.close()
    return response


@app.route('/',methods=['GET','POST'])
def index():
    print mysql.get_db()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug = True)
