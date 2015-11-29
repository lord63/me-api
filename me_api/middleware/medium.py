#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import requests
from flask import Blueprint, jsonify, json

from me_api.cache import cache
from me_api.middleware.utils import MiddlewareConfig


config = MiddlewareConfig('medium')
medium_api = Blueprint('medium', __name__, url_prefix=config.path)


@medium_api.route('/')
@cache.cached(timeout=3600)
def index():
    try:
        response = requests.get(
            'https://medium.com/{0}?format=json'.format(config.username))
    except requests.RequestException as error:
        return jsonify(error_message=str(error.message))
    if response.status_code == 200:
        return jsonify(
            medium=json.loads(response.text[16:])['payload']['latestPosts'])
    else:
        return jsonify(status_code=response.status_code)
