.. _develop:

Develop a new middleware
========================

Since many websites use OAuth2_ for their APIs, many middlewares seems
very similar to each other. If you've created a middleware, it should
be easy for you to create another one. You can take a look at `douban.py`
and `stackoverflow.py`.

For these don't need access token, can't be esay any more. Take a look
at `github.py`, `keybase.py` and `medium.py`.

I'll take instagram as an example to show you how to develop a new middleware.

1. Add the New Middleware
-------------------------

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
-------------------------

Update `me-api/me-api/app.py`, so that we can register the blueprint
according to the config file, sorted by alphabetical::

    elif module == 'instagram':
        from .middleware import instagram
        app.register_blueprint(instagram.instagram_api)

3. Update the Generate Script
-----------------------------

Update the `me-api/generate.py` so that we can generate its configuration,
middlewares are sorted by alphabetical::

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


.. _OAuth2: http://oauth.net/2/
.. _issue#6: https://github.com/lord63/me-api/issues/6