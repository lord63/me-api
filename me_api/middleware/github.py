#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from flask import Blueprint

from me_api.cache import cache
from me_api.middleware.noneedauth import NoNeedAuthView
from me_api.middleware.utils import MiddlewareConfig


config = MiddlewareConfig('github')
api_url = 'https://api.github.com/users/{0}/events/public'.format(config.me)
github_api = Blueprint('github', __name__, url_prefix=config.path)
github_api.add_url_rule(
    rule='/',
    view_func=cache.cached(timeout=300)(
        NoNeedAuthView.as_view(name='index', url=api_url)))
