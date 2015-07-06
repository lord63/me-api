# ME API

Me API is a personal API built on python and flask that allows for extensible
integrations. 

## Introduction

It is called me-api, you can build a personal website with it. With me-api,
you can fetch your photos on instagram, get your tweets from twitter, show
you code activity on github, list your blog post from medium, and etc.

## Data representation

There are two main json files: `me.json` and `modules.json`.

`me.json`

    {
        "name": "lord63",
        "join_github": "20 Aug 2013"
    }

It's all about you. Your name, your age, your hobbies, you can add anything
about youself. You'll see them on the root path "/" once you've configured
me-api.

`modules.json`

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

## How to use and run it

Clone the fresh code and go into the directory:

    $ git clone git@github.com:lord63/me-api.git
    $ cd me-api
    
Install the requirements(recommend using virtualenv):

    $ virtualenv venv
    $ source venv/bin/activate
    (venv)$ pip install -r dev-requirements.txt
    
Init the json files:

    (venv)$ python generate init

Now you have a very simple demo, run it using:

    (venv)$ python manage.py runserver
    
Open 'localhost:5000' in your broswer and take a look.

## Integration guide

Once you've init the json files, add modules should be easy, just using:

    (venv)$ python generate add
    
then follow the prompt and you are good to go.

> NOTE: 'path' should have leading slash(e.g. '/github'), and 'username' in
the prompt have an '@' should have an '@'.

## Credits

All the glories should belong to [@danfang](https://github.com/danfang),
I just port it to python.

## License

MIT.