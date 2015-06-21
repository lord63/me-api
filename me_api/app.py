#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals


from flask import Flask

from .middleware.me import me
from .cache import cache


def _register_module(app, module):
    if module == 'github':
        from .middleware import github
        app.register_blueprint(github.github_api)
    elif module == 'keybase':
        from .middleware import keybase
        app.register_blueprint(keybase.keybase_api)
    elif module == 'medium':
        from .middleware import medium
        app.register_blueprint(medium.medium_api)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    cache.init_app(app)

    modules = config.modules['modules']
    app.register_blueprint(me)
    for module in modules.keys():
        _register_module(app, module)

    return app
