import random

class Paras:


	char_list = ['1', '2', '3', '4', '5', '6', 
			'7', '8', '9', 'Enter', '0', '100']
	titel = "Rate die Zahl"

	def __init__(self):

		self.zufall = 0
		self.eingabe_zähler = 0
		self.event_list = []
		self.btn_list = []
		self.eingabe_ok = True
		self.geknackt = False

	def erhöhe_eingabezaehler(self):
		self.eingabe_zähler +=1	

	def anzahl_eingaben(self):
		self.event_list.append(self.eingabe_zähler)	

	def init_eingabezaehler(self):
		self.eingabe_zähler = 0	

	def init_zufall(self):
		self.zufall = random.randint(1, 100)

	def mische_buttons(self):
		random.shuffle(self.btn_list)

	def werte_erste_eingabe(self, input):
		if input == "Enter":
			self.eingabe_ok = False	
		else:
			self.eingabe_ok = True

	def werte_zweite_eingabe(self,past,present):
		if present == '100' or past == '100' and not present == 'Enter':
			self.eingabe_ok = False
		elif present == '0' and past == '0':
			self.eingabe_ok = False
		elif present == 'Enter' and past == '0':
			self.eingabe_ok = False
		else:
			self.eingabe_ok = True	