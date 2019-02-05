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

INSERT INTO recipes (name, youtube_link)
VALUES ("Fluffy French Toast","https://www.youtube.com/watch?v=58_5h4Kym4Y");

INSERT INTO directions (recipes_id, name)
VALUES (2,"Measure flour into a large mixing bowl. Slowly whisk in the milk. Whisk in the salt, eggs, cinnamon, vanilla extract and sugar until smooth.");

INSERT INTO directions (recipes_id, name)
VALUES (2,"Heat a lightly oiled griddle or frying pan over medium heat.");

INSERT INTO directions (recipes_id, name)
VALUES (2,"Soak bread slices in mixture until saturated. Cook bread on each side until golden brown. Serve hot.");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (2,"All-purpose flour","1/4","Cup");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (2,"Milk","1","Cup");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (2,"Salt","1","Pinch");

INSERT INTO ingredients (recipes_id, name,quantity)
VALUES (2,"Eggs","3",);

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (2,"Ground Cinnamon","1/2","Teaspoon");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (2,"While Surag","1","Tablespoon");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (2,"Beard","12","Slices");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (2,"Salt","1","Pinch");

INSERT INTO allergens (recipes_ID, name)
VALUES (2,"Oats");

INSERT INTO course (recipes_ID, name)
VALUES (2,"Breakfast");

INSERT INTO recipes (name, youtube_link)
VALUES ("Cream Of Broccoli Soup","https://www.youtube.com/watch?v=_VzN2wG5XS0");

INSERT INTO course (recipes_ID, name)
VALUES (3,"Lunch");

INSERT INTO directions (recipes_id, name)
VALUES (3,"Melt 2 tablespoons butter in medium sized stock pot, and saute onion and celery until tender. Add broccoli and broth, cover and simmer for 10 minutes.");

INSERT INTO directions (recipes_id, name)
VALUES (3,"Pour the soup into a blender, filling the pitcher no more than halfway full. Hold down the lid of the blender with a folded kitchen towel, and carefully start the blender, using a few quick pulses to get the soup moving before leaving it on to puree. Puree in batches until smooth and pour into a clean pot. Alternately, you can use a stick blender and puree the soup right in the cooking pot.");

INSERT INTO directions (recipes_id, name)
VALUES (3,"In small saucepan, over medium-heat melt 3 tablespoons butter, stir in flour and add milk. Stir until thick and bubbly, and add to soup. Season with pepper and serve.");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (3,"Butter","2","Tablespoons");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (3,"Onion","1","Chopped");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (3,"Celery Stalk","1","Chopped");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (3,"Chicken Broth","3","Cups");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (3,"Broccoli Florets","8","Cups");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (3,"Butter","3","Tablespoons");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (3,"All-Purpose Flour","3","Tablespoons");

INSERT INTO ingredients (recipes_id, name,quantity,unit_of_measurement)
VALUES (3,"Mile","2","Cups");

INSERT INTO ingredients (recipes_id, name)
VALUES (3,"Ground Black Pepper");

INSERT INTO course (recipes_ID, name)
VALUES (3,"Lunch");
