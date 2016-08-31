#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Writter():
	"""a class to normalize all output in console"""

	verbose = False



	def printed(method):
		"""decorator to check if the self.verbose is true """
		def wrapper(cls, *args):
			if cls.verbose:
				return method(cls, *args)
		return wrapper



	@classmethod
	@printed
	def event(cls, text):
		"""print an event"""
		print('\r\n- {}'.format(text))



	@classmethod
	@printed
	def sql_log(cls, sql_query, data=None):
		"""print an SQL log"""
		# if data exists , I replace them into `complete_sql_query`
		if data:
			for key, value in data.items():
				search = ':{}'.format(key)
				replace = '`{}`'.format(value)
				sql_query = sql_query.replace(search, replace)

		print('\t{}'.format(sql_query))


