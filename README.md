# CS50W - Final Project - Recipes
This web app will help you to cook and enjoy some Italian recipes.
App is designed for getting advance of feature of Django in Back End and plain
JavaScript in Front End

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
- pipfile & pipfile.lock: file created from pipenv
- README.md: documentation
- requirements.txt: Python dependencies
- .gitignore: file and folder not synchronized in git
```
/final/capstone
```
