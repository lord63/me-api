#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function

import sys
import json
from os import path
from collections import defaultdict


if sys.version_info.major == 2:
    get_input = raw_input
else:
    get_input = input
# Json files should be under me_api folder, so get the abspath.
PATH = path.join(path.dirname(path.abspath(__file__)), 'me_api')
# Template file for modules.
TEMPLATE = {
    "github": {
        "path": "Input the path(e.g. /github): ",
        "data": {
            "me": "Input the username(e.g. lord63): "
        }
    },
    "medium": {
        "path": "Input the path(e.g. /medium): ",
        "data": {
            "me": "Input the username(e.g. @lord63): "
        }
    }
}


def config_module(module):
    """Config module from user input."""
    default_conf = TEMPLATE[module]
    for key, value in default_conf.items():
        if isinstance(value, dict):
            for inner_key, inner_value in value.items():
                default_conf[key][inner_key] = get_input(inner_value)
        else:
            default_conf[key] = get_input(value)
    return default_conf


def init():
    """Initialize the me.json and modules.json."""
    print("Initialize me.json.")
    with open(path.join(PATH, 'me.json'), 'w') as f:
        me = {'name': get_input("Input your name: ")}
        json.dump(me, f, indent=4)
    print("Done: generate me.json.\n")

    print("Initialize modules.json.")
    chosen_modules = get_input(
        "Please choose modules from the following:\n"
        "\t{0}.\n"
        "Seperate then with a space: ".format(', '.join(TEMPLATE.keys()))
    ).split()
    with open(path.join(PATH, 'modules.json'), 'w') as f:
        modules = defaultdict(dict)
        for module in chosen_modules:
            print("\nConfig {0} module...".format(module))
            modules['modules'][module] = config_module(module)
        json.dump(modules, f, indent=4)
    print('\nDone: generate modules.json.')


def update():
    """Update the module settings in modules.json."""
    pass


def add():
    """Add a new module to modules.json."""
    pass


if __name__ == '__main__':
    argument = sys.argv[1]

    if argument == 'init':
        init()
    elif argument == 'update':
        update()
    elif argument == 'add':
        add()
    else:
        print("I don't know what you are talking about.\n"
              "Argument should be 'init' or 'update' or 'add'.")
