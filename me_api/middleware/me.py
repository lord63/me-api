#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from flask import Blueprint, jsonify

from me_api.configs import Config


me = Blueprint('me', __name__)


@me.route('/')
def index():
    routers = [module_config['path'] for module_config in
               Config.modules['modules'].values()]
    return jsonify(me=Config.me, routers=routers)
