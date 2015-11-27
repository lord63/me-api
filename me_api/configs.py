#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json
from os import path


class Config(object):
    CACHE_TYPE = 'null'

    cwd = path.abspath(path.dirname(__file__))
    if path.exists(path.join(cwd, 'me.json')):
        with open(path.join(cwd, 'me.json')) as me:
            me = json.load(me)
    else:
        me = json.loads('{}')
    if path.exists(path.join(cwd, 'modules.json')):
        with open(path.join(cwd, 'modules.json')) as modules:
            modules = json.load(modules)
    else:
        modules = json.loads('{"modules":{}}')


class DevelopConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    CACHE_TYPE = 'redis'


class TestingConfig(Config):
    TESTING = True
