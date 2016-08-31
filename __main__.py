#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import run, view, route, template



def main():


	@route('/')
	def tasks():
		name = "tasks"
		return template('<b>Hello {{name}}</b>!', name=name)



	@route('/hello/<name>')
	@view('index.tpl')
	def index(name):
		context = {'name' : name}
		return context

	run(host='localhost', port=12345, reloader=True)


if __name__ == '__main__':
	main()