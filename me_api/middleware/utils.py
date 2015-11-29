#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    middleware/utils.py
    ~~~~~~~~~~~~~~~~~~

    Provide some convenient tools for the middlewares.

"""

from __future__ import absolute_import

from functools import wraps

from me_api.configs import Config


class MiddlewareConfig(object):
    """Get config for the given middleware."""
    def __init__(self, name):
        self.config = Config.modules['modules'][name]

    def __getattr__(self, attr):
        if attr in self.config:
            return self.config[attr]
        if attr in self.config['data']:
            return self.config['data'][attr]


def token_required(config):
    """The index view for each middleware must have a token in the config.

    :param config: the config for the middleware.
    """
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if not config.access_token:
                return "Need access token, please authenticate your app first."
            return func(*args, **kwargs)
        return inner
    return wrapper


def reject_duplicated_auth(config):
    """The authorization view for each middleware should reject authenticating
    again if there's a token in the config.

    :param config: the config for the middleware.
    """
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if config.access_token:
                return "You've already had an access token in the config file."
            return func(*args, **kwargs)
        return inner
    return wrapper
