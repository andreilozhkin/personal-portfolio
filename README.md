# Personal Portfolio built with Django (Python)

[Live demo](https://ilozhkin.com)

This portfolio is built with [Django](https://github.com/django/django) and lots of love. Although it is my personal portfolio, feel free to fork and use as you wish.

## Installation

1. Clone repo: `git clone https://https://github.com/lozhkinandrei/personal-portfolio`
2. Switch to newly created folder: `cd personal-portfolio`
3. Install dependencies: `pip install -r requirements.txt`


## Setting Up
1. `python manage.py migrate`
2. Create superuser: `python manage.py createsuperuser`


## Adding Information (Optional)
1. Run server: `python manage.py runserver`
2. Login in admin site [localhost:8000/admin](http://localhost:8000/admin)
3. Add your first and last name for superuser you just created.
4. Create profile:
    - country* (just two letters, e.g. Russia => RU )
    - city* (full name)
5. Add your education, jobs and projects.
6. Add site meta data for SEO purposes.
7. Generate multiple size favicon [here](https://www.favicon-generator.org/), download archive and extract files in static/favicon folder

Once everything is done visit [home page](http://localhost:8000). ⛄️❤️
