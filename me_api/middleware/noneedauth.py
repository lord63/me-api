#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    middleware/noneedauth.py
    ~~~~~~~~~~~~~~~~~~

    The basic pluggable view for those services that don't need access token.

"""

from __future__ import absolute_import

from flask import jsonify
from flask.views import View
import requests


class NoNeedAuthView(View):
    methods = ['GET']

    def __init__(self, url):
        self.url = url

    def dispatch_request(self):
        # TODO: how to handle exception and error, see issue#1.
        try:
            response = requests.get(self.url)
        except requests.RequestException as error:
            return jsonify(error_message=str(error.message))
        if response.status_code == 200:
            return jsonify(github=response.json())
        else:
            return jsonify(status_code=response.status_code)
