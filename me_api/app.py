#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals


from flask import Flask

from .middleware.me import me
from .cache import cache


def _register_module(app, module):
    if module == 'douban':
        from .middleware import douban
        app.register_blueprint(douban.douban_api)
    elif module == 'github':
        from .middleware import github
        app.register_blueprint(github.github_api)
    elif module == 'instagram':
        from .middleware import instagram
        app.register_blueprint(instagram.instagram_api)
    elif module == 'keybase':
        from .middleware import keybase
        app.register_blueprint(keybase.keybase_api)
    elif module == 'medium':
        from .middleware import medium
        app.register_blueprint(medium.medium_api)
    elif module == 'stackoverflow':
        from .middleware import stackoverflow
        app.register_blueprint(stackoverflow.stackoverflow_api)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    cache.init_app(app)

    modules = config.modules['modules']
    app.register_blueprint(me)
    for module in modules.keys():
        _register_module(app, module)

    return app
