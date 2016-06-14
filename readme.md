#pomodore_manager


A simply pomodore manager written with Python and his Tkinter & Sqlite3 librairy.

The purpose is simple:
1. you create a task
2. you can create a infinite subtasks (you right-click on a task then add)
3. you can edit task in the view panel (just writte and it will be saved in live)

*This project is a way to learn Python langage, Sqlite3 database & Tkinter interface.*



##Instalation

This project is written with standards packages. To launch it, you just have to run in your terminal:

    python main.py

But if you have an older version that Python 2.5, be sure to install sqlite library before:

    pip install sqlite

I try to support old and new version. This is why I run it on old version on my Windows laptop & a new version on my Linux Mint.




> "The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s.[1] The technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks." ![a pomore timer](https://fr.wikipedia.org/wiki/Technique_Pomodoro#/media/File:Il_pomodoro.jpg "A pomodore timer") [Wikipedia](https://en.wikipedia.org/wiki/Pomodoro_Technique)

## UnitTests

I love TDD approach. You can run all test with this command `python -m unittest test.task_test`


##future

I want to implement markdown editing in tkinter view.