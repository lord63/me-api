#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import requests
from flask import Blueprint, jsonify

from me_api.configs import Config
from me_api.cache import cache


config = Config.modules['modules']['github']
path, username = config['path'], config['data']['me']
github_api = Blueprint('github', __name__)


@github_api.route(path)
@cache.cached(timeout=300)
def github():
    # TODO: how to handle exception and error, see issue#1.
    try:
        response = requests.get(
            'https://api.github.com/users/{0}/events/public'.format(username))
    except requests.RequestException as error:
        return jsonify(error_message=str(error.message))
    if response.status_code == 200:
        return jsonify(github=response.json())
    else:
        return jsonify(status_code=response.status_code)
