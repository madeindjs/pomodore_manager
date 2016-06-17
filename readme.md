pomodore_manager
=================

A simply pomodore manager written with Python and his Tkinter & Sqlite3 librairy.

> "The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s.[1] The technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks." ![a pomore timer](https://fr.wikipedia.org/wiki/Technique_Pomodoro#/media/File:Il_pomodoro.jpg "A pomodore timer") [Wikipedia](https://en.wikipedia.org/wiki/Pomodoro_Technique)



The purpose is simple:

1. you create a task
2. you can create an infinite subtasks (right-click on a task then add)
3. you can edit task in the view panel (just writte and it will be saved in live)

*This project is a way to learn Python langage, Sqlite3 database & Tkinter interface.*



Installation & run
------------------

### run without installation

This project not need an instalation and is written with standards Python libraries. To run it quickly:

    git clone https://github.com/madeindjs/pomodore_manager.git
    python pomodore_manager


### installation with cx_freeze (alpha)

You can build this project into a standalone file with **cx_freeze**. Follow theses steps:

    sudo pip apt-get install python-dev
    sudo pip install cx_Freeze
    git clone https://github.com/madeindjs/pomodore_manager.git
    cd pomodore_manager
    python setup.py build


Developpment
------------

### UnitTests

I love TDD approach. i try to write unit tests before write code. You can run test with this command:

    cd pomodore_manager
    python tests.py

Unit Test will create a test database `/data/test.sqlite` to ensure all function will work properly in production environment.


future
------
- [ ] make a standalone package
- [ ] implement markdown editing in tkinter view *(not sure is possible)*
- [ ] create a Python Package
- [ ] create a **console** mode
- [X] ~~create a verbose mode~~