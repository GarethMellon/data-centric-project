import os
import pymysql
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

username = os.getenv("C9_USER")

"""
Function to select data from mysql.  
Pass in sql as string and will result the data as a list
"""
def select_data(sql):
    connection = pymysql.connect(host = "localhost",
                            user = username,
                            password = "",
                            db = "recipes")
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

@app.route('/')
def index():
    # prep data for page
    recieps_sql="select course.name as course_name , recipes.ID as recipes_ID, recipes.name as recipes_name from recipes JOIN course on recipes.ID = course.recipes_ID;"
    recipes_data = select_data(recieps_sql)
    
    course_sql ="select count(ID), name as course_name from course group by course_name;"
    course_data = select_data(course_sql)
    
    return render_template("index.html",
                            page_title="Welcome to you're cooking recieps",
                            course_data = course_data,
                            recipes_data = recipes_data)

@app.route("/recieps/<recipe_ID>/")
def recipes(recipe_ID):
    data_sql = ("SELECT * from recipes where ID =" + recipe_ID)
    data = select_data(data_sql)
    return render_template("recieps.html", data = data)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)