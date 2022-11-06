learned from this video: Django Tutorials
   https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
   its code is at
   https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog
  
i extracted class 12 here
   https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog/12-Password-Reset/django_project

in venv
(Linux4.15-python3.8) pip install django
(Linux4.15-python3.8) python -m django --version
4.1.3
(Linux4.15-python3.8) django-admin
Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

If I didn't copy the problem from github, i would do
(Linux4.15-python3.8) tian@linux1:/home/tian/sitebase/github/django/blog$ django startproject drango_project

(Linux4.15-python3.8) tian@linux1:/home/tian/sitebase/github/django/blog/django_project$ tree
.
├── blog
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── static
│   │   └── blog
│   │       └── main.css
│   ├── templates
│   │   └── blog
│   │       ├── about.html
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── post_confirm_delete.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       └── user_posts.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── django_project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media
│   ├── default.jpg
│   └── profile_pics
│       ├── large.jpg
│       ├── large_rbSbk8j.jpg
│       └── pic.jpg
├── posts.json
└── users
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── signals.py
    ├── templates
    │   └── users
    │       ├── login.html
    │       ├── logout.html
    │       ├── password_reset_complete.html
    │       ├── password_reset_confirm.html
    │       ├── password_reset_done.html
    │       ├── password_reset.html
    │       ├── profile.html
    │       └── register.html
    ├── tests.py
    └── views.py

in the base subfolder django_project
__init__.py is empty. it just indicates that the folder is a python package.
manage.py - file allows us to run command-line command. leave it as it is.
settings.py - configuration, eg, database 
urls.py - web user entry points

