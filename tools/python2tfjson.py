#!/usr/bin/env python3

"""Wrapper for testing the Python modules in this directory.

   Not much error checking here as this script is meant to
   fail with a traceback on any problems.

   Markus Juenemann, 05-Jan-2020

"""

import sys
import importlib

# Amend module search path
sys.path.insert(0, "../..")
sys.path.insert(0, ".")

# Import the module
module = importlib.import_module("{}".format(sys.argv[1].replace(".py", "")))

# Print the config to standard out
print(module.config)
