#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.interface import Interface
import argparse


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("-v", "--verbose", action="store_true", help="Show SQL calls")
	args = parser.parse_args()

	interface = Interface()