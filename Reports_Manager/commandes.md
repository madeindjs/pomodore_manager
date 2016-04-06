#Visual Studio Commands



##database
###insert .csv file
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
