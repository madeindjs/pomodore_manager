#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import bottle
from bottle import run, view, route, post, get, template, request, redirect, static_file
from pomodore_manager.task import Task


def main():

	HOST = 'localhost'
	PORT = 65000
	bottle.TEMPLATES.clear()


	@route('/')
	@view('index.tpl')
	def index():
		"""show all tasks"""
		context = {'tasks' : Task.all()}
		return context



	@get('/new')
	@view('edit.tpl')
	def new():
		"""form a new task"""
		context = {'task' : None}
		return context


	@post('/new')
	def new():
		"""build a new task"""
		task = Task()
		task.name        = request.forms.name
		task.description = request.forms.description
		task.status      = request.forms.status
		task.node_id     = 0
		if task.add():
			redirect('/')



	@get('/update/<id>')
	@view('edit.tpl')
	def update(id):
		"""open a form with task's values"""
		task = Task.find_by('id',id)
		context = {'task' : task}
		return context



	@post('/update/<id>')
	def update(id):
		"""update the task and redirect to root"""
		task = Task.find_by('id',id)
		if task:
			task.name        = request.forms.get('name')
			task.description = request.forms.get('description')
			task.status      = request.forms.get('status')

			if task.update():
				redirect('/')



	@get('/delete/<id>')
	def delete(id):
		"""delete the given task"""
		task = Task.find_by('id',id)
		if task.delete():
			redirect('/')


	@post('/delete')
	def delete():
		"""delete the given task"""
		task_id = request.forms.id
		task = Task.find_by('id',task_id)
		return json.dumps({'result': task.delete() })



	@route('/static/<filename:path>')
	def server_static(filename):
		return static_file(filename, root='views/static')


	run(host=HOST, port=PORT, debug=True, reloader=True)


if __name__ == '__main__':
	main()