class Drawer:
	MAX_SIZE = 70
	SEPARATOR_CHAR = '_'

	def header(self , string = SEPARATOR_CHAR):
		self.subheader(string)
		self.line()

	def subheader(self , string = SEPARATOR_CHAR):
		nb_separator = int ( ( self.MAX_SIZE - len(string) ) /2 )
		print("{0}{1}{0}".format( self.SEPARATOR_CHAR*nb_separator ,  string ))

	def line(self):
		print(self.SEPARATOR_CHAR*self.MAX_SIZE)

	def list(self, list):
		for key in list:
			print( "    #{} - {}".format( key , list[key] ) )