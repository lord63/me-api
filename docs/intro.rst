Introduction
============

Me-api is a personal API built on python and flask that allows for extensible
integrations. It's a python port of the original Node.js version me-api_ .

It is called me-api, you can build a personal website with it. With me-api,
you can fetch your photos on instagram, get your tweets from twitter, show
you code activity on github, list your blog post from medium, and etc.

Data Representation
-------------------

There are two main json files: `me.json` and `modules.json`.

`me.json`::

    {
        "name": "lord63",
        "join_github": "20 Aug 2013"
    }

It's all about you. Your name, your age, your hobbies, you can add anything
about youself. You'll see them on the root path "/" once you've configured
me-api.

`modules.json`::

    {
        "modules": {
            "medium": {
                "path": "/blog",
                "data": {
                    "me": "@username"
                }
            },
            "github": {
                "path": "/code",
                "data": {
                    "me": "username"
                }
            }
        }
    }

Just as its name, it has many modules. Using custom middleware, you can attach
the data pulled from various social media feeds to specific endpoints in your
API. "path" is the endpoint which you want to host the middleware on, "data"
contains some other info so that we can fetch data from the site(some may need
authentication).

.. _me-api: https://github.com/danfang/me-api