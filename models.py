# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class PostModel(models.Model):
	nama_lengkap 		= models.CharField(max_length= 20)
	alamat				= models.CharField(max_length= 20)
	jenis_vespa			= models.CharField(max_length= 20)
	vespa_tahun			= models.DecimalField(max_digits = 19, decimal_places = 2)
	email 				= models.EmailField(max_length= 50)
	keluhan_costumer 	= models.TextField()
	no_telepon			= models.CharField(max_length= 20)
	saya_menyetujui		= models.BooleanField(max_length= 20)	

	def __str__(self):
		return "{}. {}".format(self.id, self.nama_lengkap)
