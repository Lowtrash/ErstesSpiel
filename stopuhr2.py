import tkinter as tk

#window = tk.Tk()
class Stopuhr():

	def __init__(self, stopuhr):
		
		self.minute = 0
		self.sekunde = 0
		self.millisekunde = 0
		self.times_string = "{:02d}:{:02d}:{:02d}".format(self.minute, 
			                                              self.sekunde, 
			                                              self.millisekunde)
		self.timestop = False
		self.stopuhr = stopuhr
		
			                                              	

	def start_stopuhr(self):
		global time
		self.millisekunde +=1
		#timestop = timestop
		self.timestop = True
		if self.millisekunde == 100:
			self.millisekunde = 0
			self.sekunde = self.sekunde + 1
		if self.sekunde == 60:
			self.sekunde = 0
			self.minute = self.minute + 1


		times_string = "{:02d}:{:02d}:{:02d}".format(self.minute, 
			                                              self.sekunde, 
			                                              self.millisekunde)	
		self.stopuhr.config(text=times_string)
		time = self.stopuhr.after(10, self.start_stopuhr)
		#print("self timestop ", self.timestop)

	def reset_stopuhr(self):
		#global time_string
		self.millisekunde= 0
		self.sekunde = 0
		self.minute = 0
		
		times_string = "{:02d}:{:02d}:{:02d}".format(self.minute, 
			                                              self.sekunde, 
			                                              self.millisekunde)	
		self.stopuhr.config(text=times_string)
		#self.stopuhr.after_cancel(time)	

	def stop_stopuhr(self):
		self.stopuhr.after_cancel(time)
		
		

#new_stopuhr = Stopuhr(stopuhr)
#new_stopuhr.start_stopuhr()