Time Manager
=================

A simply time manager written with Python and his Tkinter & Sqlite3 librairy.

The purpose is simple:

1. manage task
  * create task
  * create an infinite subtasks (right-click on a task then add)
  * edit task in the view panel (just writte and it will be saved in live)
* start / stop to work on a task
* see how many time spended  on each task 



Installation & run
------------------

### run without installation

This project not need an instalation and is written with standards Python libraries. To run it quickly:

    git clone https://github.com/madeindjs/pomodore_manager.git
    python pomodore_manager


### installation with cx_freeze (alpha)

You can build this project into a standalone file with **cx_freeze**. Follow theses steps:

    sudo apt-get install python-dev
    sudo pip install cx_Freeze
    git clone https://github.com/madeindjs/pomodore_manager.git
    cd pomodore_manager
    python setup.py build


Developpment
------------

### UnitTests

I love TDD approach. I try to write unit tests before write code. You can run test with this command:

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