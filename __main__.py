#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bottle
from bottle import run, view, route, template



def main():


	bottle.TEMPLATES.clear()


	@route('/')
	@view('index.tpl')
	def Index():
		context = {'name' : "Index"}
		return context



	@route('/tasks/new')
	@view('new.tpl')
	def new():
		context = {'name' : "New"}
		return context

	run(host='localhost', port=12345, debug=True, reloader=True)


if __name__ == '__main__':
	main()