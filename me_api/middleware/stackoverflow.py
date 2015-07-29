#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import os
import requests
from flask import Blueprint, jsonify, request, redirect

from me_api.configs import Config
from me_api.cache import cache


config = Config.modules['modules']['stackoverflow']
path = config['path']
key, client_secret, access_token, client_id = (
    config['data']['key'],
    config['data']['client_secret'],
    config['data']['access_token'],
    config['data']['client_id']
)
stackoverflow_api = Blueprint('stackoverflow', __name__,
                              url_prefix=path)


@stackoverflow_api.route('/')
@cache.cached(timeout=3600)
def stackoverflow():
    if not access_token:
        return 'Need access token, please authenticate you app first.'
    response = requests.get(
        ("https://api.stackexchange.com/me/timeline?"
         "site=stackoverflow&access_token={0}&key={1}").format(
             access_token, key)
    )
    return jsonify(stackoverflow=response.json())


@stackoverflow_api.route('/login')
def authorization():
    if access_token:
        return "You've already had an access token in the config file."
    authorization_url = 'https://stackexchange.com/oauth'
    return redirect(
        '{0}?client_id={1}&redirect_uri={2}&scope=no_expiry'.format(
            authorization_url, client_id,
            os.path.join(request.url, 'redirect')
        )
    )


@stackoverflow_api.route('/login/redirect')
def get_access_toekn():
    authorization_code = request.args.get('code', '')
    token_url = 'https://stackexchange.com/oauth/access_token'
    post_data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': request.base_url,
        'code': authorization_code
    }
    response = requests.post(token_url, data=post_data)
    return response.text
