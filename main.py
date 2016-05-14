#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.objects.task import Task
from classes.ui.interface import Interface

from classes.objects.database import Database
import argparse


if __name__ == '__main__':

	# parser = argparse.ArgumentParser()
	# parser.add_argument("-v", "--verbose", action="store_true", help="Show SQL calls")
	# args = parser.parse_args()

	interface = Interface()

	# Database().read('hello')