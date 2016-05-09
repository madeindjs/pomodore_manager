#pomodore_manager



A simply pomodore manager written in Python


> "The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s.[1] The technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks." ![a pomore timer](https://fr.wikipedia.org/wiki/Technique_Pomodoro#/media/File:Il_pomodoro.jpg "A pomodore timer") [Wikipedia](https://en.wikipedia.org/wiki/Pomodoro_Technique)


This project is a way to learn Python langage, Sqlite3 database & Tkinter interface.

##principe

You can manage you task. Each task is linked to a Category. Then you can start a **Pomodore**. A pomodore is a 20" timer. During this period you shut your phone and you work only on this specific task. When you finish the pomodore, you pass on anther task 

###Database representation

####Category

* id
* name

####Task

* id
* Category
* name

####Pomodore
* id
* Task
* Time
