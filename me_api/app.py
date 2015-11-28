#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from flask import Flask
from werkzeug.utils import import_string

from me_api.middleware.me import me
from me_api.cache import cache


middlewares = {
    'douban': 'me_api.middleware.douban:douban_api',
    'github': 'me_api.middleware.github:github_api',
    'instagram': 'me_api.middleware.instagram:instagram_api',
    'keybase': 'me_api.middleware.keybase:keybase_api',
    'medium': 'me_api.middleware.medium:medium_api',
    'stackoverflow': 'me_api.middleware.stackoverflow:stackoverflow_api',
}


def create_app(config):
    app = Flask('me_api')
    app.config.from_object(config)
    cache.init_app(app)

    modules = config.modules['modules']
    app.register_blueprint(me)
    for module in modules.keys():
        blueprint = import_string(middlewares[module])
        app.register_blueprint(blueprint)

    return app
