Pomodore Manager
=================

An other Pomodore manager written in:

* **Python** for the server and the backend logic
* **Javascript** for the dynamic view

Simply run the [Python server](http://bottlepy.org/) & open you're favourite web nagigator at [http://localhost:6500](http://localhost:6500): *a beautifull design appear.*


The purpose is simple:

1. manage task
    * create task
    * create an infinite subtasks
    * edit task in the view panel (just writte and it will be saved in live)
* start / stop to work on a task
* see how many time spended  on each task 

How magic appens?
-----------------

**Python** will use [Bottle.py](http://bottlepy.org/) library to run a small server. Then, when you'll create a task, **Python**'ll build a **SQlite** database. For the front-end, I use the standard [Jquery](http://jquery.com/) library and [interact.js](http://interactjs.io/) to create *Drag'n'Drop* effects.




Installation & run
------------------

This project not need an instalation and is written with standards Python libraries. To run it quickly:

    git clone https://github.com/madeindjs/pomodore_manager.git
    python pomodore_manager



Developpment
------------

### UnitTests

I love TDD approach. I try to write unit tests before write code. You can run test with this command:

    cd pomodore_manager
    python tests.py

Unit Test will create a test database `/data/test.sqlite` to ensure all function will work properly in production environment.

Requirements
------------

You'll need to install these python librairies

* [writer](https://pypi.python.org/pypi/writer/0.1.4), my simple package to normalize all outputs on my Python applications
* [bottle](https://pypi.python.org/pypi/bottle/0.12.9), Fast and simple WSGI-framework for small web-applications

You can do it quickly with this command `pip install -r requirements.txt`


Author
------

[Rousseau Alexandre](https://github.com/madeindjs/)

License
-------

[MIT](https://opensource.org/licenses/MIT)


future
------
- [ ] make a standalone package
- [ ] implement markdown editing in html view
- [ ] package with **cx_freeze**
- [ ] create a Python Package