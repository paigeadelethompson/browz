#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
# BEGIN LICENSE
# This file is in the public domain
# END LICENSE

import browz
import sys
import os

import gettext
gettext.textdomain('browz')

# Add project root directory (enable symlink and trunk execution)
PROJECT_ROOT_DIRECTORY = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0]))))

python_path = []
if os.path.abspath(__file__).startswith('/opt'):
    syspath = sys.path[:]  # copy to avoid infinite loop in pending objects
    for path in syspath:
        opt_path = path.replace('/usr', '/opt/extras.ubuntu.com/browz')
        python_path.insert(0, opt_path)
        sys.path.insert(0, opt_path)
if (os.path.exists(os.path.join(PROJECT_ROOT_DIRECTORY, 'browz'))
        and PROJECT_ROOT_DIRECTORY not in sys.path):
    python_path.insert(0, PROJECT_ROOT_DIRECTORY)
    sys.path.insert(0, PROJECT_ROOT_DIRECTORY)
if python_path:
    os.putenv('PYTHONPATH', "%s:%s" % (os.getenv('PYTHONPATH', ''), ':'.join(python_path)))  # for subprocesses

browz.main()
