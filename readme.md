# pomodore_manager

> "The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s.[1] The technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks." ![a pomore timer](https://fr.wikipedia.org/wiki/Technique_Pomodoro#/media/File:Il_pomodoro.jpg "A pomodore timer") [Wikipedia](https://en.wikipedia.org/wiki/Pomodoro_Technique)

A simply pomodore manager written with Python and his Tkinter & Sqlite3 librairy.

The purpose is simple:

1. you create a task
2. you can create an infinite subtasks (right-click on a task then add)
3. you can edit task in the view panel (just writte and it will be saved in live)

*This project is a way to learn Python langage, Sqlite3 database & Tkinter interface.*



## Instalation & run 

This project not need an instalation and is written with standards Python librairies. So tu run it, you just have to run in your terminal:

    python __main__.py


If you have an older version than Python 2.5, be sure to install sqlite library before:

    pip install sqlite

I try to support old and new version. This is why I run it on old version on my Windows laptop & a new version on my Linux Mint.



## UnitTests

I love TDD approach. This is why you can run all tests with this command `python -m unittest test.task_test` and verify that everything is allright


## future

- [ ] implement markdown editing in tkinter view *(not sure is possible)*
- [ ] create a Python Package
- [ ] create a **console** mode
- [X] ~~create a verbose mode~~