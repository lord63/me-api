#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from flask import Blueprint, jsonify

from me_api.configs import Config


me = Blueprint('me', __name__)


@me.route('/')
def index():
    routers = []
    for module in Config.module['modules'].values():
        routers.append(module['path'])
    return jsonify(me=Config.me, routers=routers)
