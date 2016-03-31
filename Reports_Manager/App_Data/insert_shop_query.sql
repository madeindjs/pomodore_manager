SET IDENTITY_INSERT [dbo].[Shops] ON

INSERT INTO [dbo].[Shops] (
	/*[Id], */
	[Article_id], 
	[Serie], 
	[Otp], 
	[Magasin], 
	[Adresse], 
	[Code_postal], 
	[Ville], 
	[N_sortie], 
	[Date_sm], 
	[Date_fact]
) 
VALUES (
	/*10,*/ 
	N'a', 
	N'r', 
	N'a', 
	N'gfd', 
	N'azeq', 
	N'69300', 
	N'1', 
	1, 
	N'2016-01-01 00:00:00', 
	N'2016-01-01 00:00:00'
)
SET IDENTITY_INSERT [dbo].[Shops] OFF
