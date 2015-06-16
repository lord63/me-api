#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import requests
from flask import Blueprint, jsonify

from me_api.configs import Config


config = Config.modules['modules']['github']
path, username = config['path'], config['data']['me']
github_api = Blueprint('github', __name__)


@github_api.route(path)
def github():
    response = requests.get(
        'https://api.github.com/users/{0}/events/public'.format(username))
    return jsonify(github=response.json())
