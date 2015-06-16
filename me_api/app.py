#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals


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
