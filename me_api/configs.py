#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json
from os import path


class Config(object):
    cwd = path.abspath(path.dirname(__file__))
    with open(path.join(cwd, 'me.json')) as me:
        me = json.load(me)
    with open(path.join(cwd, 'modules.json')) as modules:
        modules = json.load(modules)


class DevelopConfig(Config):
    DEBUG = True
    CACHE_TYPE = 'simple'


class ProductionConfig(Config):
    DEBUG = False
