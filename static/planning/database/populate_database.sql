INSERT INTO allergens_list (name)
VALUES ("Cereals");

INSERT INTO allergens_list (name)
VALUES ("Crustaceans ");

INSERT INTO allergens_list (name)
VALUES ("Eggs");

INSERT INTO allergens_list (name)
VALUES ("Fish");

INSERT INTO allergens_list (name)
VALUES ("Peanuts ");

INSERT INTO allergens_list (name)
VALUES ("Soybeans");

INSERT INTO allergens_list (name)
VALUES ("Milks");

INSERT INTO allergens_list (name)
VALUES ("Nuts");

INSERT INTO allergens_list (name)
VALUES ("Celery ");

INSERT INTO allergens_list (name)
VALUES ("Mustard");

INSERT INTO allergens_list (name)
VALUES ("Sesame");

INSERT INTO allergens_list (name)
VALUES ("Sulphur dioxide");

INSERT INTO allergens_list (name)
VALUES ("Lupin");

INSERT INTO allergens_list (name)
VALUES ("Molluscs ");

INSERT INTO course_list (name)
VALUES ("Appetizer");

INSERT INTO course_list (name)
VALUES ("Beverage");

INSERT INTO course_list (name)
VALUES ("Breakfast");

INSERT INTO course_list (name)
VALUES ("Brunch");

INSERT INTO course_list (name)
VALUES ("Dessert");

INSERT INTO course_list (name)
VALUES ("Entree");

INSERT INTO course_list (name)
VALUES ("Side Dish");

INSERT INTO course_list (name)
VALUES ("Snack");

INSERT INTO course_list (name)
VALUES ("Soup");

INSERT INTO course_list (name)
VALUES ("Stew");

INSERT INTO cuisine_list (name)
VALUES ("African");

INSERT INTO cuisine_list (name)
VALUES ("American");

INSERT INTO cuisine_list (name)
VALUES ("British");

INSERT INTO cuisine_list (name)
VALUES ("Caribbean");

INSERT INTO cuisine_list (name)
VALUES ("Chinese");

INSERT INTO cuisine_list (name)
VALUES ("East European");

INSERT INTO cuisine_list (name)
VALUES ("French");

INSERT INTO cuisine_list (name)
VALUES ("Greek");

INSERT INTO cuisine_list (name)
VALUES ("Indian");

INSERT INTO cuisine_list (name)
VALUES ("Irish");

INSERT INTO cuisine_list (name)
VALUES ("Italian");

INSERT INTO cuisine_list (name)
VALUES ("Japanese");

INSERT INTO cuisine_list (name)
VALUES ("Korean");

INSERT INTO cuisine_list (name)
VALUES ("mexican");

INSERT INTO cuisine_list (name)
VALUES ("middle Eastern");

INSERT INTO cuisine_list (name)
VALUES ("Portuguese");

INSERT INTO cuisine_list (name)
VALUES ("South American");

INSERT INTO cuisine_list (name)
VALUES ("Spanish");

INSERT INTO cuisine_list (name)
VALUES ("Thai");

INSERT INTO recipes (name, youtube_link)
VALUES ("Pancakes","https://www.youtube.com/watch?v=FLd00Bx4tOk");

INSERT INTO directions (recipes_id, name)
VALUES (1,"Beat eggs, oil, and milk together, and add to flour. Stir until combined.");

INSERT INTO directions (recipes_id, name)
VALUES (1,"Heat a greased griddle until drops of water sprinkled on it evaporate noisily. Pour 1/8 to 1/4 cup batter onto the griddle. Turn over with a metal spatula when bubbles begin to form on top. Cook second side to a golden brown color.");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (1,"Self-rising flour","1","Cup");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (1,"Milk","1","Cup");

INSERT INTO ingredients (recipes_id, name,quantity)
VALUES (1,"Egg","1",);

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (1,"Vegtable Oil","2","tablespoons");

INSERT INTO allergens (recipes_ID, name)
VALUES (1,"Contains Eggs");

INSERT INTO course (recipes_ID, name)
VALUES (1,"Breakfast");


