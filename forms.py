from django import forms

class ContactForm(forms.Form):
	nama_lengkap 		= forms.CharField(
		label = 'Nama Lengkap',
		max_length = 30,
		widget = forms.TextInput(
				attrs ={
				 'class':'form-control',
				 'placeholder':'masukan nama lengkap anda',
				}
			)
		)
	alamat				= forms.CharField(
		max_length = 30,
		widget = forms.TextInput(
				attrs ={
				 'class':'form-control',
				 'placeholder':'masukan alamat anda',
				}
			)
		)
	jenis_vespa			= forms.ChoiceField(
		widget = forms.RadioSelect(
			attrs={
				'class':'form-check-input',
			}),			
		choices = [
			('C','Classic'),
			('M','Matic'),
		]		
		)
	vespa_tahun			= forms.DecimalField()
	email 				= forms.EmailField(
		widget = forms.TextInput(
				attrs ={
					'class':'form-control',
					'placeholder':'harap isi dengan email aktif'
				}
			))
	keluhan_costumer 	= forms.CharField(
		widget = forms.Textarea(
					attrs ={
					'class':'form-control',
					}	
		))
	no_telepon			= forms.CharField(
		label = 'No Telepon',
		max_length = 15,
		widget = forms.TextInput(
				attrs ={
				 'class':'form-control',
				 'placeholder':'masukan nomer telepon anda',
				}
			)
		)
	saya_menyetujui		= forms.BooleanField()	

