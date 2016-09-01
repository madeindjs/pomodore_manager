#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bottle
from bottle import run, view, route, post, get, template, request, redirect, static_file
from pomodore_manager.task import Task


def main():


	bottle.TEMPLATES.clear()


	@route('/')
	@view('index.tpl')
	def Index():
		# build the Task list
		context = {'tasks' : Task.all()}
		return context



	@get('/tasks/new')
	@view('new.tpl')
	def new():
		context = {'name' : "New"}
		return context


	@post('/tasks/new')
	def new():
		task = Task()
		task.name        = request.forms.get('name')
		task.description = request.forms.get('description')
		task.status      = request.forms.get('status')
		task.node_id      = 0
		if task.add():
			redirect('/')




	@route('/static/<filename:path>')
	def server_static(filename):
		return static_file(filename, root='views/static')


	run(host='localhost', port=12345, debug=True, reloader=True)


if __name__ == '__main__':
	main()