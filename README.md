# CS50W - Final Project - Recipes
This web app will help you to cook and enjoy some Italian recipes.
App is designed for getting advance of feature of Django in Back End and plain
JavaScript in Front End.

## Distinctiveness and Complexity
This project is different from other course project's because it combine some
feature we already met in our education with new feature. The result is a more
complex and in-deep web app.

Feature:
- Register
- Login
- Logout
- Reset password (via terminal not via mail because project is in development)
- Add to favorites / Remove from favorites
- Add comment / Edit comment / Delete comment
- Admin Dashboard
- Pagination
- Shopping List: list of ingredients needed for a recipe
- Messages
- Responsive design
- Csrf security
- Test for models and routes
- API
- Fetch API

## Video

## Back End
- Python
- Django
- Pillow
- Pipenv

## Front End
- HTML
- CSS
- JavaScript

## Installation
If in your computer git is not already installed, please install git.

```bash
git clone https://github.com/dak79/cs50w-final.git

cd final

pip3 install pipenv
pipenv shell

pip3 install -r requirements.txt

cd capstone
python3 manage.py runserver
```

## Files
```
/final
```
- pipfile & pipfile.lock: file created from pipenv.
- README.md: documentation.
- requirements.txt: Python dependencies.
- .gitignore: file and folder not synchronized in git.

```
/final/capstone
```
- \_\_init\_\_.py: capstone project init file.
- asgi.py: ASGI configuration for capstone project.
- settings.py: Django settings for capstone project.
- urls.py: capstone project urls configuration.
- wsgi.py: WSGI configuration for capstone project.

```
/final/capstone/recipes
```
- \_\_init\_\_.py: recipes app init file.
- admin.py: admin dashboard for recipes app.
- apps.py: recipes app app configuration file.
- forms.py: forms models for recipes app.
- test.py: models and views tests' for recipes app.
- models.py: database models for recipes app.
- urls.py: urls for views and API endpoints for recipes app.
- views.py: views and API endpoints for recipes app.

```
/final/capstone/recipes/migrations
```
From 0001_initiat.py to 0020_alter_user_image.py files contain all migrations
done during development.

```
/final/capstone/recipes/static/css
```
- styles.css: recipes app style sheet.

```
/final/capstone/recipes/static/img/favicon
```
- favicon.io: favicon image.

```
/final/capstone/recipes/static/img/navbar
```
- avocado_192x192.png: avocado image.

```
/final/capstone/recipes/static/img/profile_image
```
In here they will be stored all files for user profile image.

```
/final/capstone/recipes/static/js
```
- index.js: JavaScript for index.html.
- main.js: JavaScript for layout.html.
- shopping_list.js: JavaScript for shopping_list.html.

```
/final/capstone/recipes/templates/recipes
```
- index.html: index template.
- layout.html: boilerplate template.
- login.html: login template.
- register.html: register template.
- shopping_list.html: shopping_list template.
- user.html: user template.

```
/final/capstone/recipes/templates/recipes/password
```
- password_reset_complete.html: password reset complete template.
- password_reset_confirm.html: password reset confirm template.
- password_reset.html: password reset template.
- reset_mail.txt: mail text for resetting password via link.

## API

|                   Endpoint                     | HTTP Method | CRUD Method |                  Result                 |
|------------------------------------------------|:-----------:|:-----------:|-----------------------------------------|
| api/v1/recipe/ingredients/<int:id>/            | GET         | READ        | Get all ingredients for a given recipes |
