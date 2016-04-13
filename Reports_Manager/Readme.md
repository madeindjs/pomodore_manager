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

#API


##Shop


###insert `.csv` file
~~~sql
BULK
INSERT Shops
FROM 'C:\Users\rousseaua\! Projets\SQL\BDD\exports_SAP\C#\2016.01.csv'
WITH
(
   FIELDTERMINATOR = ';',
   ROWTERMINATOR = '\n'
);
~~~

...with .csv file in this format:

~~~csv
1;13073;4062048;47Y0613;SUPER U LE PALAIS SUR VIENNE;AVENUE DE LIMOGES;87410;LE PALAIS SUR VIENNE;06/01/2016;06/01/2016;0
2;11735;16027278;47Y0613;SUPER U LE PALAIS SUR VIENNE;AVENUE DE LIMOGES;87410;LE PALAIS SUR VIENNE;06/01/2016;06/01/2016;0
3;11735;16027278;47Y0613;SUPER U LE PALAIS SUR VIENNE;AVENUE DE LIMOGES;87410;LE PALAIS SUR VIENNE;06/01/2016;06/01/2016;0
~~~

* Try to make improvement with [this method](http://stackoverflow.com/questions/36593116/insert-csv-file-into-sql-server-with-bulk-insert-and-reorder-columns/36594073#36594073)

##Articles



###insert `.csv` file

~~~sql
BULK
INSERT Articles
FROM 'C:\Users\rousseaua\! Projets\SQL\BDD\Base article\Base article_purged_with_SqlId.csv'
WITH
(
   FIELDTERMINATOR = ';',
   ROWTERMINATOR = '\n'
);
~~~
    
##Report

##Category





#Migrations
##shortcurts
`Add-Migration` to make migration from models  
`update-database -Verbose` to update database


##migration example
This is just an example founded [here](https://msdn.microsoft.com/fr-fr/data/jj591621.aspx)

~~~c#
public override void Up() 
{ 
   CreateTable( 
       "Posts", 
       c => new 
       { 
          PostId = c.Int(nullable: false, identity: true), 
          Title = c.String(maxLength: 200), 
          Content = c.String(), 
          BlogId = c.Int(nullable: false), 
       }
   ) 
    .PrimaryKey(t => t.PostId) 
    .ForeignKey("Blogs", t => t.BlogId, cascadeDelete: true) 
    .Index(t => t.BlogId) 
    .Index(p => p.Title, unique: true); 
    AddColumn("Blogs", "Rating", c => c.Int(nullable: false, defaultValue: 3)); 
} 
 
public override void Down() 
{ 
    DropIndex("Posts", new[] { "Title" }); 
    DropIndex("Posts", new[] { "BlogId" }); 
    DropForeignKey("Posts", "BlogId", "Blogs"); 
    DropColumn("Blogs", "Rating"); 
    DropTable("Posts"); 
} 
~~~