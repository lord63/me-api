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
    (venv)$ pip install -r requirements/requirements.txt

Configure Me-api
----------------

Init the json files::

    (venv)$ python generate init

Answer several questions according to the prompt. It will help you generate
`me.json` and `modules.json` in the `me_api/me_api/` folder. When choosing
middlewares, I suggest using github for demo purpose, very easy to set up,
only username required.

Note that 'path' should have a leading slash(e.g. '/github'), and 'username'
in the prompt have an '@' should have an '@'.

Once generated the config file, now you have a very simple demo,
run it using::

    (venv)$ python manage.py runserver

Open 'localhost:5000' in your broswer and take a look.

Security
--------

It is suggested to use HTTPS for your site that powered by me-api when
authenticating the middlewares. Also, when configure the new app in the
app page(e.g. twitter's app page), remember to grant your app access only
to the resources that they really need, high permission is not necessary
sometimes(e.g. can delete or edit your content).
