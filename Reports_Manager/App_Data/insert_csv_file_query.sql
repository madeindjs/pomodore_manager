BULK
 INSERT Shops
FROM 'C:\Users\rousseaua\! Projets\SQL\BDD\exports_SAP\#2015.12.csv'
WITH
(
FIELDTERMINATOR = ';',
ROWTERMINATOR = '\n'
);
