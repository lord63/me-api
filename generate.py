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
    "douban": {
        "path": "Input the path(e.g. /douban): ",
        "data": {
            "me": "Input the username(e.g. xvid73): ",
            "client_id": "Input the 'API Key' for douban: ",
            "client_secret": "Input the 'Secret' for douban: ",
            "access_token": ""
        }
    },
    "github": {
        "path": "Input the path(e.g. /github): ",
        "data": {
            "me": "Input the username(e.g. lord63): "
        }
    },
    "instagram": {
        "path": "Input the path(e.g. /photos): ",
        "data": {
            "client_id": "Input the 'Client ID' for instagram: ",
            "client_secret": "Input the 'Client Secret' for instagram: ",
            "access_token": ""
        }
    },
    "keybase": {
        "path": "Input the path(e.g. /keybase): ",
        "data": {
            "me": "Input the username(e.g. lord63): "
        }
    },
    "medium": {
        "path": "Input the path(e.g. /medium): ",
        "data": {
            "me": "Input the username(e.g. @lord63): "
        }
    },
    "stackoverflow": {
        "path": "Input the path(e.g. /stackoverflow): ",
        "data": {
            "key": "Input the 'Key' for stackoverflow: ",
            "client_id": "Input the 'Client ID' for stackoverflow: ",
            "client_secret": "Input the 'Client Secret' for stackoverflow: ",
            "access_token": ""
        }
    }
}


def config_module(module):
    """Config module from user input."""
    default_conf = TEMPLATE[module]
    default_conf['path'] = get_input(default_conf['path'])
    for key, value in default_conf['data'].items():
        if key == 'access_token': continue
        default_conf['data'][key] = get_input(value)
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
        "Seperate with a space: ".format(', '.join(TEMPLATE.keys()))
    ).split()
    with open(path.join(PATH, 'modules.json'), 'w') as f:
        modules = defaultdict(dict)
        for module in chosen_modules:
            print("\nConfig {0} module...".format(module))
            modules['modules'][module] = config_module(module)
        json.dump(modules, f, indent=4)
    print('\nDone: generate modules.json.')


def add():
    """Add a new module to modules.json."""

    # Read configurations from modules.json then overwrite it.
    # http://stackoverflow.com/a/2424410/4890577
    with open(path.join(PATH, 'modules.json'), 'r+') as f:
        modules = json.load(f)
        not_configed = (set(TEMPLATE.keys()) -
                        set(modules['modules'].keys()))
        if not not_configed:
            print("You've used all the available modules.")
            return
        else:
            chosen_modules = get_input(
                "Please choose modules from the following:\n"
                "\t{0}.\n"
                "Seperate with a space: ".format(', '.join(not_configed))
            ).split()
            for module in chosen_modules:
                print("\nConfig {0} module...".format(module))
                modules['modules'][module] = config_module(module)
        f.seek(0)
        json.dump(modules, f, indent=4)
        f.truncate()
        print("\nAdd {0} to modules.json".format(', '.join(chosen_modules)))


if __name__ == '__main__':
    argument = sys.argv[1]

    if argument == 'init':
        init()
    elif argument == 'add':
        add()
    else:
        print("I don't know what you are talking about.\n"
              "Argument should be 'init' or 'add'.")
