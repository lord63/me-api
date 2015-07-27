#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import os
import requests
from flask import Blueprint, jsonify, request, redirect

from me_api.configs import Config
from me_api.cache import cache


config = Config.modules['modules']['douban']
path = config['path']
me, client_secret, access_token, client_id = config['data'].values()
douban_api = Blueprint('douban', __name__, url_prefix=config['path'])


@douban_api.route('/')
@cache.cached(timeout=3600)
def douban():
    if not access_token:
        return 'Need access token, please authenticate you app first.'
    response = requests.get(
        "https://api.douban.com/shuo/v2/statuses/user_timeline/{0}".format(me),
        headers={'Authorization': 'Bearer ' + access_token})
    return jsonify(douban=response.json())


@douban_api.route('/login')
def authorization():
    if access_token:
        return "You've already had an access token in the config file."
    authorization_url = 'https://www.douban.com/service/auth2/auth'
    return redirect(
        '{0}?client_id={1}&redirect_uri={2}&response_type={3}'.format(
            authorization_url, client_id,
            os.path.join(request.url, 'redirect'), 'code')
    )


@douban_api.route('/login/redirect')
def get_access_toekn():
    authorization_code = request.args.get('code', '')
    token_url = 'https://www.douban.com/service/auth2/token'
    post_data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_url': os.path.join(request.url),
        'grant_type': 'authorization_code',
        'code': authorization_code
    }
    response = requests.post(token_url, data=post_data)
    return response.text
