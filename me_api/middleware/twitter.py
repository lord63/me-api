#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import requests
from flask import Blueprint, jsonify
from requests_oauthlib import OAuth1

from me_api.cache import cache
from me_api.middleware.utils import (MiddlewareConfig, token_required)


config = MiddlewareConfig('twitter')
twitter_api = Blueprint('twitter', __name__, url_prefix=config.path)


@twitter_api.route('/')
@cache.cached(timeout=60*5)
@token_required(config)
def index():
    api_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    auth = OAuth1(
        client_key=config.consumer_key,
        client_secret=config.consumer_secret,
        resource_owner_key=config.access_token,
        resource_owner_secret=config.access_token_secret
    )
    response = requests.get(api_url, auth=auth)
    return jsonify(twitter=response.json())
