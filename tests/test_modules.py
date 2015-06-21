#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import unittest
import json

from me_api.app import create_app
from me_api.configs import TestingConfig


class MeAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig).test_client()

    def test_index(self):
        rv = self.app.get('/')
        assert 'me' in json.loads(rv.data.decode()).keys()
        assert 'routers' in json.loads(rv.data.decode()).keys()
        assert (len(TestingConfig.modules['modules'].keys()) ==
                len(json.loads(rv.data.decode())['routers']))
