#Report Manager

Report manager is **CMS** (
**C**ontent **M**anager **S**ystem) who allow technicians to Create, Read, Update & Delete (CRUD System) reports on web based interface.

1. the user **connect** him on the web portail (is forbidden to access on this without login)
* he **search** a shop by name, town, cabinets selled, serial number, etc..
* he **consult** the shop (info, cabinets, reports, etc..)
* he **create** a report on cabinets in the shop
* managers can **view** some statistics about reports, problems, users, etc..


##about development
* written in **C#**
* use **ASP.NET MVC 5** framework
* need Microsoft **SQL Server**

##my configuration

* Windows 7 Entreprise 64-bits
*  Microsoft **Visual Studio Express 2015** pour le web: *Version 14.0.23107.0 D14REL*
* Microsoft .NET Framework: *Version 4.6.01055*
* ASP.NET and Web Tools 2015 (RC1 Update 1): *version 14.1.11120.0*
* NuGet manager: *version 3.4.0*
* SQL Server Data Tools: *version 14.0.50616.0*

#shortcurts & commands

##databases

###insert `.csv` file
    BULK
    INSERT Articles
    FROM 'C:\Users\rousseaua\! Projets\SQL\BDD\Base article\Base article_purged_with_SqlId.csv'
    WITH
    (
        FIELDTERMINATOR = ';',
        ROWTERMINATOR = '\n'
    );

###Migrations
`Add-Migration` to make migration from models  
`update-database -Verbose` to update database

`String alew = String.new`