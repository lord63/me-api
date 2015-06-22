#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import requests
from flask import Blueprint, jsonify, json

from me_api.configs import Config
from me_api.cache import cache


config = Config.modules['modules']['medium']
path, username = config['path'], config['data']['me']
medium_api = Blueprint('medium', __name__)


@medium_api.route(path)
@cache.cached(timeout=3600)
def medium():
    try:
        response = requests.get(
            'https://medium.com/{0}?format=json'.format(username))
    except requests.RequestException as error:
        return jsonify(error_message=str(error.message))
    if response.status_code == 200:
        return jsonify(
            medium=json.loads(response.text[16:])['payload']['latestPosts'])
    else:
        return jsonify(status_code=response.status_code)
