#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template

def main():

	@route('/home')
	def home():
		return template('<h1>{{content}}</h1>', content='Reload works!')

		

	@route('/hello/<name>')
	def index(name):
		return template('<b>Hello {{name}}</b>!', name=name)

	run(host='localhost', port=12345, reloader=True)


if __name__ == '__main__':
	main()