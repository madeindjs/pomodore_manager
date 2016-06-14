#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

from view.writter import Writter
from view.interface import Interface
from classes.database import Database



if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("-v", "--verbose", action="store_true", help="Show SQL calls")
	args = parser.parse_args()

	if args.verbose:
		Writter.verbose = True

	interface = Interface()