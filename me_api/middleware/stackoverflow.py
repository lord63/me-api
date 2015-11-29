#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import requests
from flask import Blueprint, jsonify, request, redirect

from me_api.cache import cache
from me_api.middleware.utils import (MiddlewareConfig, token_required,
                                     reject_duplicated_auth)


config = MiddlewareConfig('stackoverflow')
stackoverflow_api = Blueprint('stackoverflow', __name__,
                              url_prefix=config.path)


@stackoverflow_api.route('/')
@cache.cached(timeout=3600)
@token_required(config)
def index():
    response = requests.get(
        ("https://api.stackexchange.com/me/timeline?"
         "site=stackoverflow&access_token={0}&key={1}").format(
             config.access_token, config.key)
    )
    return jsonify(stackoverflow=response.json())


@stackoverflow_api.route('/login')
@reject_duplicated_auth(config)
def authorization():
    authorization_url = 'https://stackexchange.com/oauth'
    return redirect(
        '{0}?client_id={1}&redirect_uri={2}&scope=no_expiry'.format(
            authorization_url, config.client_id,
            os.path.join(request.base_url, 'redirect')
        )
    )


@stackoverflow_api.route('/login/redirect')
def get_access_token():
    authorization_code = request.args.get('code', '')
    token_url = 'https://stackexchange.com/oauth/access_token'
    post_data = {
        'client_id': config.client_id,
        'client_secret': config.client_secret,
        'redirect_uri': request.base_url,
        'code': authorization_code
    }
    response = requests.post(token_url, data=post_data)
    return response.text
