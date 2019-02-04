import os
import pymysql
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

username = os.getenv("C9_USER")

connection = pymysql.connect(host = "localhost",
                            user = username,
                            password = "",
                            db = "recipes")

"""
Function to select data from mysql.  
Pass in sql as string and will result the data as a list
"""
def select_data(sql):
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

@app.route('/')
def index():
    sql="select * from recipes;"
    data = select_data(sql)
    
    return render_template("index.html",
                            page_title="Home Page", 
                            data = data)

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)