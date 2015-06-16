#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    me-api
    ~~~~~~

    An extensible, personal API with custom integrations.
    It's a python port of the original node.js me-api.

    :copyright: (c) 2015 by lord63.
    :license: MIT, see LICENSE for more details.
"""

__title__ = "me-api"
__version__ = '0.1.0'
__author__ = "lord63"
__license__ = "MIT"
__copyright__ = "Copyright 2015 lord63"


from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    from .middleware.me import me
    from .middleware.github import github_api
    from .middleware.medium import medium_api

    app.register_blueprint(me)
    app.register_blueprint(github_api)
    app.register_blueprint(medium_api)

    return app
