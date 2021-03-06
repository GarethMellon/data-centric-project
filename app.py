import os
import pymysql
from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)
app.secret_key = 'This_is_a_Secret'

username = os.getenv("C9_USER")

"""
Function to select data from mysql.  
Pass in sql as string and will result the data as a list
"""
def select_data(sql):
    #localhost connection
    """
    connection = pymysql.connect(host = "localhost",
                            user = username,
                            password = "",
                            db = "recipes")
    """
    # Heroku / ClearDB connection
    connection = pymysql.connect(host = 'eu-cdbr-west-02.cleardb.net',
                                db = 'heroku_da99daf1f492997',
                                user = "b7185d11cb25b9",
                                password = '110588d0')
    
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()
        
def update_data(sql):
    #localhost connection
    """
    connection = pymysql.connect(host = "localhost",
                            user = username,
                            password = "",
                            db = "recipes")
    """
    # Heroku / ClearDB connection
    connection = pymysql.connect(host = 'eu-cdbr-west-02.cleardb.net',
                                db = 'heroku_da99daf1f492997',
                                user = "b7185d11cb25b9",
                                password = '110588d0')
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()

"""
Pass in a string of text (as text) and uses list of invalid characters.
Returns the text with the invalid character striped out.
"""
def remove_invalid_characters(text):
    invalid_character_set = ['!','"','$','%','^','&','*','{','}',']','[','~','#',':',';',"'",'~','?','>','<',"\\",'|']
    num = 0 
    while num < len(invalid_character_set):
        if invalid_character_set[num] in text:
            text = text.replace(invalid_character_set[num], "")
            flash_message = ("Please note we have removed the invalid character '{}' from you're text").format(invalid_character_set[num])
            flash(flash_message)
        num += 1
    return text

"""
Pass in a string as text and check if it is empty.
Returns True if it is
"""
def text_is_none(text):
    if not text:
        return True
    else:
        return False
        
"""
Function to parase a youtube link so we can embed it on the page
"""
def parse_youtube_url(url):
    url = url[0]['youtube_link']
    if url:
        url = url.replace('https://www.youtube.com/watch?v=','https://www.youtube.com/embed/')
        return url
    else:
        return None

"""
All pages route and functions below
"""

@app.route('/')
def index():
    # prep data for page
    recieps_sql="select course.name as course_name , recipes.ID as recipes_ID, recipes.name as recipes_name from recipes JOIN course on recipes.ID = course.recipes_ID AND course.delete = 0;"
    recipes_data = select_data(recieps_sql)
    
    course_sql ="select count(ID), name as course_name from course where course.delete = 0 group by course_name;"
    course_data = select_data(course_sql)
    
    course_list_sql = "SELECT course_list.ID AS course_list_ID, course_list.name AS course_list_name from course_list;"
    course_list_data = select_data(course_list_sql)
    
    return render_template("index.html",
                            page_title="Welcome To Cooking Recieps",
                            course_data = course_data,
                            recipes_data = recipes_data,
                            course_list_data = course_list_data)

#### Recieps routes and functions
@app.route("/recieps/<recipe_ID>/")
def recieps(recipe_ID):
    # prep data for page
    recipes_sql = ("SELECT * FROM recipes WHERE recipes.ID =" + recipe_ID + " AND recipes.delete = '0';")
    recipes_data = select_data(recipes_sql)
    
    directions_sql = ("SELECT * FROM directions WHERE recipes_ID =" + recipe_ID + " AND directions.delete = '0';")
    directions_data = select_data(directions_sql)
    
    ingredients_sql = ("SELECT * FROM ingredients WHERE recipes_ID =" + recipe_ID + " AND ingredients.delete = '0';")
    ingredients_data = select_data(ingredients_sql)
    
    cuisine_sql = ("SELECT * FROM cuisine WHERE recipes_ID =" + recipe_ID + " AND cuisine.delete = '0';")
    cuisine_data = select_data(cuisine_sql)
    
    course_sql = ("SELECT * FROM course WHERE recipes_ID =" + recipe_ID + " AND course.delete = '0';")
    course_data = select_data(course_sql)
    
    allergens_sql = ("SELECT * FROM allergens WHERE recipes_ID =" + recipe_ID + " AND allergens.delete = '0';")
    allergens_data = select_data(allergens_sql)
    
    #get and parse youtube link for the UI
    youtube_link_sql = ("SELECT youtube_link FROM recipes WHERE recipes.ID =" + recipe_ID + " AND recipes.delete = '0';")
    youtube_link = select_data(youtube_link_sql)
    if youtube_link :
        youtube_link = parse_youtube_url(youtube_link)
    else:
        youtube_link = None
    
    return render_template("recieps.html",
                            page_title="Edit Recipe",
                            recipes_data = recipes_data,
                            directions_data = directions_data,
                            ingredients_data = ingredients_data,
                            cuisine_data = cuisine_data,
                            course_data = course_data,
                            allergens_data = allergens_data,
                            recipe_ID = recipe_ID,
                            youtube_link = youtube_link)
                            
@app.route("/delete_recipe/<recipe_ID>/")
def delete_recipe(recipe_ID):
    
    allergens_sql = "UPDATE allergens SET allergens.delete = 1 WHERE allergens.recipes_ID = {};".format(recipe_ID)
    course_sql = "UPDATE course SET course.delete = 1 WHERE course.recipes_ID = {};".format(recipe_ID)
    cuisine_sql = "UPDATE cuisine SET cuisine.delete = 1 WHERE cuisine.recipes_ID = {};".format(recipe_ID)
    directions_sql = "UPDATE directions SET directions.delete = 1 WHERE directions.recipes_ID = {};".format(recipe_ID)
    ingredients_sql = "UPDATE ingredients SET ingredients.delete = 1 WHERE ingredients.recipes_ID = {};".format(recipe_ID)
    recipes_sql = "UPDATE recipes SET recipes.delete = 1 WHERE recipes.ID = {};".format(recipe_ID)
    
    update_data(allergens_sql)
    update_data(course_sql)
    update_data(cuisine_sql)
    update_data(directions_sql)
    update_data(ingredients_sql)
    update_data(recipes_sql)
    
    return redirect(url_for('index'))

## Add new recipe
@app.route("/new_recipe", methods = ["POST"])
def new_recipe():
    recipe_name = request.form.get("recipe_name")
    course_name = request.form.get('selection')
    # Check is the user input is null
    if text_is_none(recipe_name) == True or text_is_none(course_name) == True:
        flash('You must enter some text')
        return redirect(url_for('index'))
    else:
        # strip out invalid characters
        recipe_name = remove_invalid_characters(recipe_name)
        
        recipe_sql = "INSERT INTO recipes (name, youtube_link) VALUES ('{}','{}');".format(recipe_name, '' )
        select_recipe_ID = "SELECT recipes.ID from recipes where recipes.name = '{}';".format(recipe_name)
    
        update_data(recipe_sql)
        recipe_ID = select_data(select_recipe_ID)
        course_sql = "INSERT INTO course (recipes_ID, name) VALUES ('{}', '{}');".format(recipe_ID[0]['ID'], course_name)
        update_data(course_sql)
    return redirect(url_for('recieps',
                            recipe_ID = recipe_ID[0]['ID'] ))
                            
@app.route("/youtube_link/<recipe_ID>")
def youtube_link(recipe_ID):
    sql = "select ID as recipe_ID, name as recipe_name, youtube_link as recipe_youtube_link from recipes WHERE recipes.ID = {};".format(recipe_ID)
    recipe_data = select_data(sql)
    
    return render_template('youtube_link.html',
                            page_title = "YouTube Link",
                            recipe_data = recipe_data,
                            recipe_ID = recipe_ID)
                            
@app.route("/save_youtube_link/<recipe_ID>", methods = ["POST"])
def save_youtube_link(recipe_ID):
    youtube_link = request.form.get('youtube_link_name')
    # check if user entered a null 
    if text_is_none(youtube_link) == True:
        flash('You must enter some text')
        return redirect(url_for('recieps',
                                recipe_ID = recipe_ID))
    else:
        youtube_link = youtube_link.strip()
        sql = "UPDATE recipes SET youtube_link = '{}' WHERE ID = {};".format(youtube_link, recipe_ID)
        update_data(sql)
        
    return redirect(url_for('recieps',
                            recipe_ID = recipe_ID))
                            
@app.route("/delete_youtube_link/<recipe_ID>")
def delete_youtube_link(recipe_ID):
    youtube_link = request.form.get('youtube_link_name')
    sql = "UPDATE recipes SET youtube_link = '' WHERE ID = {};".format(recipe_ID)
    update_data(sql)
        
    return redirect(url_for('recieps',
                            recipe_ID = recipe_ID))
    
## Routes to add edit and delete recieps

#### Directions routes and functions
@app.route("/directions/<recipe_ID>/<direction_ID>/")
def directions(recipe_ID, direction_ID):
    # prep data for page
    directions_sql = "SELECT recipes.ID AS recipe_ID, recipes.name AS recipe_name, directions.ID AS direction_ID, directions.name AS direction_name FROM recipes JOIN directions ON recipes.ID = directions.recipes_ID WHERE recipes.ID = " + recipe_ID + " AND directions.ID = " + direction_ID +";"
    directions_data = select_data(directions_sql)
    
    return render_template("directions.html", 
                            page_title="Edit Directions",
                            directions_data = directions_data)

## Routes to add edit and delete directions                            
@app.route("/edit_direction/<recipe_ID>/<direction_ID>/", methods = ["POST"])
def edit_direction(recipe_ID, direction_ID):
    direction_text = request.form.get("direction_name")
    
    # strip out invalid characters and strip out any spaces at the start and end of the input
    direction_text = remove_invalid_characters(direction_text)
    direction_text = direction_text.strip()

    update_sql = "UPDATE directions SET name = '{}' WHERE directions.ID = {};".format(direction_text, direction_ID)
    update_data(update_sql)
    return redirect(url_for('recieps',
                            recipe_ID = recipe_ID))

@app.route("/add_direction/<recipe_ID>/")
def add_direction(recipe_ID):
    directions_sql = "SELECT recipes.ID AS recipe_ID, recipes.name AS recipe_name FROM recipes WHERE recipes.ID = " + recipe_ID + ";"
    directions_data = select_data(directions_sql)
    return render_template("directions.html", 
                            page_title="Add New Direction",
                            directions_data = directions_data)
    
@app.route("/add_new_direction/<recipe_ID>", methods = ["POST"])
def add_new_direction(recipe_ID):
    direction_text = request.form.get("direction_name").strip()
    # Check if the user input is null
    if text_is_none(direction_text) == True:
        flash('You must enter some text')
        return redirect(url_for('recieps',
                            recipe_ID = recipe_ID))
    else:
        # string out invalid character and blank spaces at the start and end
        direction_text = remove_invalid_characters(direction_text)
        direction_text = direction_text.strip()
        
        update_sql = "INSERT INTO directions (recipes_ID, name) VALUES ({},'{}');".format(recipe_ID, direction_text)
        update_data(update_sql)
    return redirect(url_for('recieps',
                            recipe_ID = recipe_ID))
    
@app.route("/delete_direction_from_recipe/<recipe_ID>/<direction_ID>/")
def delete_direction_from_recipe(recipe_ID, direction_ID):
    course_update_sql = "UPDATE directions SET directions.delete = 1 WHERE directions.ID = {};".format(direction_ID)
    update_data(course_update_sql)
    return redirect(url_for("recieps", 
                            recipe_ID = recipe_ID))

#### Ingredients routes and functions               
@app.route("/ingredients/<recipe_ID>/<ingredient_ID>/")
def ingredients(recipe_ID, ingredient_ID):
    # prep data for page
    ingredients_sql = "SELECT recipes.ID AS recipe_ID, recipes.name AS recipe_name, ingredients.ID AS ingredients_ID, ingredients.name AS ingredients_name, ingredients.quantity AS ingredient_quantity, ingredients.unit_of_measurement AS ingredients_unit_of_measurement FROM recipes JOIN ingredients ON recipes.ID = ingredients.recipes_ID WHERE recipes.ID = " + recipe_ID + " AND ingredients.ID = " + ingredient_ID +";"
    ingredient_data = select_data(ingredients_sql)
    
    return render_template("ingredients.html", 
                        page_title="Edit Ingredients",
                        ingredient_data = ingredient_data)

## Routes to add edit and delete ingredients 
@app.route("/edit_ingredient/<recipe_ID>/<ingredient_ID>/", methods = ["POST"])
def edit_ingredient(recipe_ID, ingredient_ID):
    ingredient_text = request.form.get("ingredients_name")
    ingredient_quantity = request.form.get("ingredient_quantity")
    ingredient_unit_of_measurement = request.form.get("ingredients_unit_of_measurement")
    
    #strip out invalid chatacters and strip out blank spaces at the start and end.
    ingredient_text = remove_invalid_characters(ingredient_text)
    ingredient_text = ingredient_text.strip()
    
    update_sql = "UPDATE ingredients SET name = '{}', quantity = '{}', unit_of_measurement ='{}' WHERE ingredients.ID = {};".format(ingredient_text, ingredient_quantity, ingredient_unit_of_measurement, ingredient_ID)
    update_data(update_sql)
    return redirect(url_for('recieps',
                            recipe_ID = recipe_ID))

@app.route("/add_ingredient/<recipe_ID>/")
def add_ingredient(recipe_ID):
    ingredient_sql = "SELECT recipes.ID AS recipe_ID, recipes.name AS recipe_name FROM recipes WHERE recipes.ID = " + recipe_ID + ";"
    ingredient_data = select_data(ingredient_sql)
    return render_template("ingredients.html", 
                            page_title="Add New Ingredient",
                            ingredient_data = ingredient_data)
                            
@app.route("/add_ingredient_to_recipe/<recipe_ID>/", methods = ["POST"])
def add_ingredient_to_recipe(recipe_ID):
    ingredient_text = request.form.get("ingredients_name")
    ingredient_quantity = request.form.get("ingredient_quantity")
    ingredient_unit_of_measurement = request.form.get("ingredients_unit_of_measurement")
    # check if the string is null
    if text_is_none(ingredient_text) == True:
        flash('You must enter some text')
        return redirect(url_for("recieps", 
                                recipe_ID = recipe_ID))
    else:
        #strip out invalid chatacters and strip out blank spaces at the start and end.
        ingredient_text = remove_invalid_characters(ingredient_text)
        ingredient_text = ingredient_text.strip()
        
        update_sql = "INSERT INTO ingredients (recipes_ID, name, quantity, unit_of_measurement) VALUES('{}','{}','{}','{}');".format(recipe_ID, ingredient_text, ingredient_quantity, ingredient_unit_of_measurement)
        update_data(update_sql)

    return redirect(url_for("recieps", 
                            recipe_ID = recipe_ID))
                            
@app.route("/delete_ingredient_from_recipe/<recipe_ID>/<ingredient_ID>/")
def delete_ingredient_from_recipe(recipe_ID, ingredient_ID):
    update_sql = "UPDATE ingredients SET ingredients.delete = 1 WHERE ingredients.ID = {};".format(ingredient_ID)
    print(update_sql)
    update_data(update_sql)
    return redirect(url_for("recieps", 
                            recipe_ID = recipe_ID))

#### Course routes and functions
@app.route("/course/<recipe_ID>/<course_ID>/")
def course (recipe_ID, course_ID):
    # prep data for page
    course_sql = "SELECT recipes.ID AS recipe_ID, recipes.name AS recipe_name, course.ID AS course_ID, course.name AS course_name FROM recipes JOIN course ON recipes.ID = course.recipes_ID WHERE recipes.ID = '{}' AND course.delete = '0'".format(recipe_ID)
    course_data = select_data(course_sql)
    
    course_list_sql = "SELECT course_list.ID AS course_list_ID, course_list.name AS course_list_name from course_list;"
    course_list_data = select_data(course_list_sql)
    
    return render_template("course.html",
                            page_title = "Edit Courses",
                            course_data = course_data,
                            course_list_data = course_list_data)

## Routes to add edit and delete courses 
@app.route("/add_course_to_recipe/<recipe_ID>/<course_ID>/", methods = ["POST"])
def add_course_to_recipe(recipe_ID, course_ID):
    course_to_add = request.form.get("selection")
    # check is the user input is null
    if text_is_none(course_to_add) == True:
        flash("You need to select a course from the list")
        return redirect(url_for('recieps',
                                recipe_ID = recipe_ID))
    else:
        course_update_sql = "INSERT INTO course (recipes_ID, name) VALUES ('{}','{}');".format(recipe_ID, course_to_add)
        update_data(course_update_sql)
    
    return redirect(url_for("recieps", 
                            recipe_ID = recipe_ID))

@app.route("/delete_course_from_recipe/<recipe_ID>/<course_ID>/")
def delete_course_from_recipe(recipe_ID, course_ID):
    course_update_sql = "UPDATE course SET course.delete = 1 WHERE course.ID = {};".format(course_ID)
    update_data(course_update_sql)
    return redirect(url_for("recieps", recipe_ID = recipe_ID))
    
@app.route("/course_list")
def course_list():
    # prep data for page
    course_list_sql = "SELECT course_list.ID AS course_list_ID, course_list.name AS course_list_name from course_list;"
    course_list_data = select_data(course_list_sql)
    
    return render_template("course_list.html",
                            page_title = "Course List",
                            course_list_data = course_list_data)

@app.route("/update_course_list/", methods = ["POST"])
def update_course_list():
    course_list_name = request.form.get("course_list_name")
    # check if use input is null
    if text_is_none(course_list_name) == True:
        flash('You must enter some text')
        return redirect(url_for('course_list'))
    else:
        # strip out invalid characters and stip out leading and ending spaces
        course_list_name = remove_invalid_characters(course_list_name)
        course_list_name = course_list_name.strip()
        
        course_list_update_sql = "INSERT INTO course_list (course_id, name) VALUES ( 0, '" + course_list_name +"');"
        update_data(course_list_update_sql)
            
    return redirect(url_for("course_list"))

@app.route("/delete_course_list/<course_list_ID>/")
def delete_course_list(course_list_ID):
    sql = "DELETE from course_list where ID = '{}';".format(course_list_ID)
    update_data(sql)
    return redirect(url_for('course_list'))
    
#### Cuisine routes and functions
@app.route("/new_cuisine/<recipe_ID>/")
def new_cuisine (recipe_ID):
    # prep data for page
    
    recipes_sql = ("SELECT ID as recipe_ID, name as recipe_name FROM recipes WHERE recipes.ID =" + recipe_ID + " AND recipes.delete = '0';")
    recipes_data = select_data(recipes_sql)
    
    cuisine_list_sql = "SELECT cuisine_list.ID AS cuisine_list_ID, cuisine_list.name AS cuisine_list_name from cuisine_list;"
    cuisine_list_data = select_data(cuisine_list_sql)
    
    return render_template("cuisine.html",
                            page_title = "New Cuisine",
                            cuisine_list_data = cuisine_list_data,
                            recipes_data = recipes_data, recipe_ID = recipe_ID)

@app.route("/cuisine/<recipe_ID>/")
def cuisine (recipe_ID):
    # prep data for page
    cuisine_sql = "SELECT recipes.ID AS recipe_ID, recipes.name AS recipe_name, cuisine.ID AS cuisine_ID, cuisine.name AS cuisine_name FROM recipes JOIN cuisine ON recipes.ID = cuisine.recipes_ID WHERE recipes.ID = " + recipe_ID + " AND cuisine.delete = '0';"
    cuisine_data = select_data(cuisine_sql)
    
    cuisine_list_sql = "SELECT cuisine_list.ID AS cuisine_list_ID, cuisine_list.name AS cuisine_list_name from cuisine_list;"
    cuisine_list_data = select_data(cuisine_list_sql)
    
    return render_template("cuisine.html",
                            page_title = "Edit Cuisine",
                            cuisine_data = cuisine_data,
                            cuisine_list_data = cuisine_list_data, recipe_ID = recipe_ID)

## Routes to add edit and delete cuisine 
@app.route("/add_cuisine_to_recipe/<recipe_ID>/", methods = ["POST"])
def add_cuisine_to_recipe(recipe_ID):
    cuisine_to_add = request.form.get("selection")
    # check if the user input is null
    if text_is_none(cuisine_to_add) == True:
        flash('You must enter some text')
        return redirect(url_for("recieps", 
                                recipe_ID = recipe_ID))
    else:
        cuisine_update_sql = "INSERT INTO cuisine (recipes_ID, name) VALUES ('{}','{}');".format(recipe_ID, cuisine_to_add)
        update_data(cuisine_update_sql)
    
    return redirect(url_for("recieps", 
                            recipe_ID = recipe_ID))

@app.route("/delete_cuisine_from_recipe/<recipe_ID>/<cuisine_ID>/")
def delete_cuisine_from_recipe(recipe_ID, cuisine_ID):
    cuisine_update_sql = "UPDATE cuisine SET cuisine.delete = 1 WHERE cuisine.ID = {};".format(cuisine_ID)
    update_data(cuisine_update_sql)
    return redirect(url_for("recieps", recipe_ID = recipe_ID))
    
@app.route("/cuisine_list")
def cuisine_list():
    # prep data for page
    cuisine_list_sql = "SELECT cuisine_list.ID AS cuisine_list_ID, cuisine_list.name AS cuisine_list_name from cuisine_list;"
    cuisine_list_data = select_data(cuisine_list_sql)
    
    return render_template("cuisine_list.html",
                            page_title = "Course List",
                            cuisine_list_data = cuisine_list_data)

@app.route("/update_cuisine_list/", methods = ["POST"])
def update_cuisine_list():
    cuisine_list_name = request.form.get("cuisine_list_name")
    
    # check for a null value in the user input
    if text_is_none(cuisine_list_name) == True:
        flash('You must enter some text')
        return redirect(url_for('cuisine_list'))
    else:
        # strip out invalid characters and stip out leading and ending spaces
        cuisine_list_name = remove_invalid_characters(cuisine_list_name)
        cuisine_list_name = cuisine_list_name.strip()
        
        cuisine_list_update_sql = "INSERT INTO cuisine_list (cuisine_ID, name) VALUES ( 0, '" + cuisine_list_name +"');"
        update_data(cuisine_list_update_sql)
            
    return redirect(url_for("cuisine_list"))

@app.route("/delete_cuisine_list/<cuisine_list_ID>/")
def delete_cuisine_list(cuisine_list_ID):
    sql = "DELETE from cuisine_list where ID = '{}';".format(cuisine_list_ID)
    update_data(sql)
    return redirect(url_for('cuisine_list'))
    

#### Allergens routes and functions
@app.route("/allergens/<recipe_ID>/")
def allergens (recipe_ID):
    # prep data for page
    allergens_sql = "SELECT recipes.ID AS recipe_ID, recipes.name AS recipe_name, allergens.ID AS allergens_ID, allergens.name AS allergens_name FROM recipes JOIN allergens ON recipes.ID = allergens.recipes_ID WHERE recipes.ID = " + recipe_ID + " AND allergens.delete = 0;"
    allergens_data = select_data(allergens_sql)
    
    allergens_list_sql = "SELECT allergens_list.ID AS allergens_list_ID, allergens_list.name AS allergens_list_name from allergens_list;"
    allergens_list_data = select_data(allergens_list_sql)
    
    return render_template("allergens.html",
                            page_title = "Edit Allergens",
                            allergens_data = allergens_data,
                            allergens_list_data = allergens_list_data,
                            recipe_ID = recipe_ID)
    
## Routes to add edit and delete allergens     
@app.route("/new_allergen/<recipe_ID>/")
def new_allergen (recipe_ID):
    # prep data for page
    
    recipes_sql = ("SELECT ID as recipe_ID, name as recipe_name FROM recipes WHERE recipes.ID =" + recipe_ID + " AND recipes.delete = '0';")
    recipes_data = select_data(recipes_sql)
    
    allergens_list_sql = "SELECT allergens_list.ID AS allergens_list_ID, allergens_list.name AS allergens_list_name from allergens_list;"
    allergens_list_data = select_data(allergens_list_sql)
    
    return render_template("allergens.html",
                            page_title = "New Allergens",
                            recipes_data = recipes_data,
                            allergens_list_data = allergens_list_data, 
                            recipe_ID = recipe_ID)
                            
@app.route("/add_allergens_to_recipe/<recipe_ID>/", methods = ["POST"])
def add_allergens_to_recipe(recipe_ID):
    allergens_to_add = request.form.get("selection")
    # check is the user input is null
    if text_is_none(allergens_to_add):
        flash('You must enter some text')
        return redirect(url_for("recieps", 
                                recipe_ID = recipe_ID))
    else:
        allergens_update_sql = "INSERT INTO allergens (recipes_ID, name) VALUES ('{}','{}');".format(recipe_ID, allergens_to_add)
        update_data(allergens_update_sql)
    
    return redirect(url_for("recieps", 
                            recipe_ID = recipe_ID))

@app.route("/delete_allergens_from_recipe/<recipe_ID>/<allergens_ID>/")
def delete_allergens_from_recipe(recipe_ID, allergens_ID):
    allergens_update_sql = "UPDATE allergens SET allergens.delete = 1 WHERE allergens.ID = {};".format(allergens_ID)
    update_data(allergens_update_sql)
    return redirect(url_for("recieps", recipe_ID = recipe_ID))
                            
@app.route("/allergens_list")
def allergens_list():
    # prep data for page
    allergens_list_sql = "SELECT allergens_list.ID AS allergens_list_ID, allergens_list.name AS allergens_list_name from allergens_list;"
    allergens_list_data = select_data(allergens_list_sql)
    
    return render_template("allergens_list.html",
                            page_title = "Allergens List",
                            allergens_list_data = allergens_list_data)
                            
@app.route("/update_allergens_list/", methods = ["POST"])
def update_allergens_list():
    allergen_list_name = request.form.get("allergens_list_name")
     # check for a null value in the user input
    if text_is_none(allergen_list_name) == True:
        flash('You must enter some text')
        return redirect(url_for('allergens_list'))
    else:
        # strip out invalid characters and strip out leading and ending spaces
        allergen_list_name = remove_invalid_characters(allergen_list_name)
        allergen_list_name = allergen_list_name.strip()
        
        allergen_list_update_sql = "INSERT INTO allergens_list (allergens_id, name) VALUES ( 0, '" + allergen_list_name +"');"
        update_data(allergen_list_update_sql)
            
    return redirect(url_for("allergens_list"))
    
@app.route("/delete_allergens_list/<allergens_list_ID>/")
def delete_allergens_list(allergens_list_ID):
    sql = "DELETE from allergens_list where ID = '{}';".format(allergens_list_ID)
    update_data(sql)
    return redirect(url_for('allergens_list'))
                       
                       
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=False)