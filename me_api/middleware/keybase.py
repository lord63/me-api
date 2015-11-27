#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from flask import Blueprint

from me_api.cache import cache
from me_api.middleware.base import BasicView
from me_api.middleware.utils import MiddlewareConfig


config = MiddlewareConfig('keybase')
api_url = (("https://keybase.io/_/api/1.0/user/lookup.json?"
            "usernames={0}").format(config.me))
keybase_api = Blueprint('keybase', __name__, url_prefix=config.path)
keybase_api.add_url_rule(
    rule='/',
    view_func=cache.cached(timeout=86400)(
        BasicView.as_view(name='index', url=api_url)))
