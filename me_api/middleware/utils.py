#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from me_api.configs import Config


class MiddlewareConfig(object):
    def __init__(self, name):
        self.config = Config.modules['modules'][name]

    def __getattr__(self, attr):
        if attr in self.config:
            return self.config[attr]
        if attr in self.config['data']:
            return self.config['data'][attr]
