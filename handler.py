#!/bin/env python

from pyroutes import application

from tvseries import *

if __name__ == '__main__':
    from pyroutes.utils import devserver
    devserver(application)
