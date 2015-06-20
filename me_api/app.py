#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals


from flask import Flask

from .middleware.me import me
from .middleware import github, keybase, medium
from .cache import cache


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    cache.init_app(app)

    modules = config.modules['modules']
    blueprints = {
        'github': github.github_api,
        'keybase': keybase.keybase_api,
        'medium': medium.medium_api
    }

    app.register_blueprint(me)
    for module in modules.keys():
        app.register_blueprint(blueprints[module])

    return app
