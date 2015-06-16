#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import os

from flask.ext.script import Manager

from me_api.app import create_app
from me_api.configs import DevelopConfig, ProductionConfig


if os.environ.get('Flask_APP') == 'production':
    app = create_app(ProductionConfig)
else:
    app = create_app(DevelopConfig)

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
