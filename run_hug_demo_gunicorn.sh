#!/bin/bash

# using gunicorn
gunicorn hello:__hug_wsgi__
