#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: hello.py
Author: r.zach.lamberty@gmail.com
Created: 2016-07-15

Description:
    demoing hug for apis

Usage:
    <usage>

"""

import argparse
import os

import eri.logging as logging
import hug
import jinja2


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

logger = logging.getLogger(__name__)
logging.configure()

html = hug.get(output=hug.output_format.html)

HERE = os.path.dirname(os.path.realpath(__file__))
TEMP_DIR = os.path.join(HERE, 'templates')
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMP_DIR))


# ----------------------------- #
#   routes                      #
# ----------------------------- #

@hug.cli()
@hug.get(examples='name=Zach&age=31')
@hug.local()
def happy_birthday(name: hug.types.text, age: hug.types.number, hug_timer=3):
    """says happy bday to a user"""
    return {
        'message': "happy {} bday {}!".format(age, name),
        'took': float(hug_timer)
    }


@html
@hug.get(examples='name=Zach&age=31')
def hbd_html(name: hug.types.text, age: hug.types.number, hug_timer=3):
    """says happy bday to a user"""
    return JINJA_ENV.get_template('index.html').render(name=name)


if __name__ == '__main__':
    happy_birthday.interface.cli()
