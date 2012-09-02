from django.db import models

class Information(models.Model):

	first_name = models.CharField( max_length=30 )
	last_name = models.CharField( max_length=30 )

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name
	
	#def sign_up( self, first, last ):
		
		
