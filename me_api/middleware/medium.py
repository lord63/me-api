#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json

import requests
from flask import Blueprint, jsonify

from me_api.configs import Config


config = Config.module['modules']['medium']
path, username = config['path'], config['data']['me']
medium_api = Blueprint('medium', __name__)


@medium_api.route(path)
def medium():
    response = requests.get(
        'https://medium.com/{0}?format=json'.format(username))
    return jsonify(
        medium=json.loads(response.text[16:])['payload']['latestPosts'])
