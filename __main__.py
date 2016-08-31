#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template

def main():

	@route('/hello/<name>')
	def index(name):
		return template('<b>Hello {{name}}</b>!', name=name)

	run(host='localhost', port=12345)


if __name__ == '__main__':
	main()