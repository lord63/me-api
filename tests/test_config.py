#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from me_api.app import create_app
from me_api.configs import DevelopConfig, ProductionConfig, TestingConfig


def test_develop_config():
    app = create_app(DevelopConfig)
    assert app.config['DEBUG'] is True


def test_production_config():
    app = create_app(ProductionConfig)
    assert app.config['DEBUG'] is False


def test_testing_config():
    app = create_app(TestingConfig)
    assert app.config['TESTING'] is True
