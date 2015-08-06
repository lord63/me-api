Qucikstart
==========

This page gives your a guide for how to set up the basic configuration
for me-api. Head over to :ref:`integrate` for further information.

Install from Souce Code
-----------------------

Clone the fresh code and go into the directory::

    $ git clone git@github.com:lord63/me-api.git
    $ cd me-api

Install the requirements(recommend using virtualenv)::

    $ virtualenv venv
    $ source venv/bin/activate
    (venv)$ pip install -r requirements.txt

Configure Me-api
----------------

Init the json files::

    (venv)$ python generate init

answer several questions according to the prompt.

Now you have a very simple demo, run it using::

    (venv)$ python manage.py runserver

Open 'localhost:5000' in your broswer and take a look.