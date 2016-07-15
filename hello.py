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


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

logger = logging.getLogger(__name__)
logging.configure()

html = hug.get(output=hug.output_format.html)


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
    return """
    <h1>Happy Birthday {}, you old fuck!
    """.format(name)


if __name__ == '__main__':
    happy_birthday.interface.cli()
