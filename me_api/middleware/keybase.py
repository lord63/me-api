#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import requests
from flask import Blueprint, jsonify

from me_api.configs import Config
from me_api.cache import cache


config = Config.modules['modules']['keybase']
path, username = config['path'], config['data']['me']
keybase_api = Blueprint('keybase', __name__, url_prefix=path)


@keybase_api.route('/')
@cache.cached(timeout=900)
def keybase():
    try:
        response = requests.get(
            "https://keybase.io/_/api/1.0/user/lookup.json?"
            "usernames={0}".format(username))
    except requests.RequestException as error:
        return jsonify(error_message=str(error.message))
    if response.status_code == 200:
        return jsonify(keybase=response.json())
    else:
        return jsonify(status_code=response.status_code)
