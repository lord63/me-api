.. _develop:

Develop a new middleware
========================

Since many websites use OAuth2_ for their APIs, many middlewares seems
very similar to each other. If you've created a middleware, it should
be easy for you to create another one. You can take a look at `douban.py`
and `stackoverflow.py`.

For these don't need access token, can't be esay any more. Take a look
at `github.py`, `keybase.py` and `medium.py`.

Build a universal middleware
----------------------------

This chapter is for those public service, such as Instagram, github and etc.
I'll take instagram as an example to show you how to develop a universal
middleware.

1. Add the New Middleware
^^^^^^^^^^^^^^^^^^^^^^^^^

Add a new middleware in `me-api/me-api/middlewares` folder, in this
example, we add a new middleware named instagram: `instagram.py`.

I'll take this one into details::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    from __future__ import absolute_import, unicode_literals

    # Import modules you need.
    import os
    import requests
    from flask import Blueprint, jsonify, request, redirect

    # Import config and cache.
    from me_api.configs import Config
    from me_api.cache import cache

    # Get configuration from our `modules.json`.
    config = Config.modules['modules']['instagram']
    path = config['path']
    client_secret, access_token, client_id = (
        config['data']['client_secret'],
        config['data']['access_token'],
        config['data']['client_id']
    )
    # Our main blueprint.
    instagram_api = Blueprint('instagram', __name__, url_prefix=path)

    # Get information once we have access token, remember to set
    # a proper timeout for the middleware cache.
    @instagram_api.route('/')
    @cache.cached(timeout=3600)
    def instagram():
        pass

    # Get authorization_code.
    @instagram_api.route('/login')
    def authorization():
        pass

    # Get access token we need.
    @instagram_api.route('/login/redirect')
    def get_access_toekn():
        pass

2. Register the Blueprint
^^^^^^^^^^^^^^^^^^^^^^^^^

Update `me-api/me-api/app.py`, so that we can register the blueprint
according to the config file, sorted by alphabetical::

    elif module == 'instagram':
        from .middleware import instagram
        app.register_blueprint(instagram.instagram_api)

3. Update the Generate Script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update the `TEMPLATE` in `me-api/generate.py` so that we can generate its
configuration, middlewares are sorted by alphabetical::

    "instagram": {
        "path": "Input the path(e.g. /photos): ",
        "data": {
            "client_id": "Input the 'Client ID' for instagram: ",
            "client_secret": "Input the 'Client Secret' for instagram: ",
            "access_token": ""
        }
    }

`path`: where you host your middleware, for example, you can host instagram
middleware on `/photos`.

`data`: contain data we need when authorize our app, data should have a flat
structure, don't add another dict in `data`, see `issue#6`_.

Note that we need the access token, just leave it blank as showing above.

Build a specific middleware
---------------------------

This is for some specific usages, for example, develop a custom middleware
only for your own sites, cause they don't born with API support, you have to
roll your own API.

I'll take my blog as an example to show you how to develop a specific middleware.

1. Add the New Middleware
^^^^^^^^^^^^^^^^^^^^^^^^^

In fact, it's not difficult at all, just parse your blog posts and make an dict
then return it. The result is under your control, make the modify as you like.
A thousand people may have one thousand different kinds of blogs. I can't cover
them all, but I hope you can get some inspirations from this example. Remember,
it's your site, it's your own API, feel free to build something.

Here is the custom middleware for my blog: `blog.py`::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    from __future__ import absolute_import, unicode_literals

    import requests
    from flask import Blueprint, jsonify
    from lxml import html

    from me_api.configs import Config
    from me_api.cache import cache

    # We only need a path.
    path = Config.modules['modules']['blog']['path']
    blog_api = Blueprint('blog', __name__)


    @blog_api.route(path)
    @cache.cached(timeout=3600)
    def blog():
        try:
            response = requests.get('http://blog.lord63.com')
            tree = html.fromstring(response.text)
            titles = [title.strip() for title in
                      tree.xpath('//ul[@class="posts"]/li/h2/a/text()')
                      if title.strip()]
            dates = tree.xpath('//small[@class="datetime muted"]/span/text()')
            blog = {"name": "lord63's blog", "powered_by": "pelican",
                    "author": "lord63", "theme": "pelican-scribble-hex",
                    "site": "http://blog.lord63.com"}
            blog["posts"] = [{"title": title, "date": date} for title, date in
                             zip(titles, dates)]
        except requests.RequestException as error:
            return jsonify(error_message=str(error.message))
        if response.status_code == 200:
            return jsonify(blog=blog)
        else:
            return jsonify(status_code=response.status_code)

2. Register the Blueprint
^^^^^^^^^^^^^^^^^^^^^^^^^

Update `me-api/me-api/app.py`, so that we can register the blueprint
according to the config file, sorted by alphabetical::

    elif module == 'blog':
        from .middleware import blog
        app.register_blueprint(blog.blog_api)

3. Update the Generate Script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can skip it, because this middleware is used only by youself.

Update the `TEMPLATE` in `me-api/generate.py`, middlewares are sorted
by alphabetical::

    "blog": {
        "path": "Input the path(e.g. /blog): "
    }


.. _OAuth2: http://oauth.net/2/
.. _issue#6: https://github.com/lord63/me-api/issues/6
