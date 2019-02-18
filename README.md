# Your Project's Name

Project Nane : Recipes Cooking page.
This project allows a user to add, store and retrives informaion on cooking recipes.  A user can used add a youtube video to each recipe.


## Planning

# Planning board
https://trello.com/b/TipYwEPg/data-centric-project-clone

# Wireframes
Located in static/planning/wireframes
Wireframes built in Balsamiq.

# Database Schema
Located in static/planning/database
DB Schema built in https://www.dbdesigner.net/designer

# backgroundimage taken from
https://www.inc.com/karen-schrier/4-brilliant-ideas-you-should-steal-from-food-industry.html

# Colour Picker
https://material.io/tools/color/#!/?view.left=0&view.right=0&primary.color=01579B&secondary.color=F9A825

 
## UX
 
Most pages are a single column design.  UI works on mobile and ipad (tested in chrome emulator)

## Features

### Existing Features
 - Add recipes (with directions, ingredients, course, cuisine and allergies informaion)
 - Deleted recipe (and all its linked informaion)
 - all course list, allergen list and cuisine list data (for user in drop down selectors)
 - add youtube links to recipes

### Planned Features
- Edit or delete youtube links
- add author informaion
- add cooking estimates
- add the ability to rank recipes and mark a favorite
- UI automation via cucumber

### Current Bugs
- BUg where sometimes when creating a new recipe, no recipes loads. Only workaround for now is to delete and try again with a different recipe name


## Technologies Used

- [html](https://jquery.com)

- [CSS](https://jquery.com)

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [Materalize CSS](https://materializecss.com)
    - The project materialize for its main stylings.

- [Javascript](https://www.javascript.com/)

- [Python](https://www.python.org/)

- [Flask](http://flask.pocoo.org/)
    - The project uses to build the pages and pass information between the front and back end. 

- [MySQL](https://www.mysql.com/)
    - The project uses MySQL as the database engine.

- [MySQL WorkBench](https://www.mysql.com/products/workbench/)

- [ClearDB#](https://w2.cleardb.net/)
    - The project uses ClearDB for the production database.

- [Git](https://git-scm.com/)
    - The project uses Git for version control.

- [GitHub](https://github.com/)

- [Heroku](https://heroku.com)
    - The project uses heroku for production build of the app.

- [Balsamiq](https://balsamiq.com/)
    - The project used this for wireframe planning.

- [dbdesigner](https://www.dbdesigner.net/)
    - The project uses to plan the database scheme.

- [Trello](https://trello.com/)
    - The project uses Trello to manage project tasks.

- [Cucumber](https://cucumber.io/)
    - The project cucumber for manual, and planned automated testings on the UI.




## Testing

Manual testing outlined in/static/planning/cucumber_tests.txt

This will also be used for automating the UI with Selenium.

## Deployment

Project deplyed on Heroku ( https://data-centric-project-4.herokuapp.com/ )
No extra tasked need to run the app.

## Credits

### Content
- recipe data taken from https://www.allrecipes.com/

### Media
- backgroundimage taken from https://www.inc.com/karen-schrier/4-brilliant-ideas-you-should-steal-from-food-industry.html
