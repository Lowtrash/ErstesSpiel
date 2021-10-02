import tkinter as tk
window = tk.Tk()

class DreiFenster():
	#Erzeugt den Rahmen
	ereignissfeld = tk.Frame(master=window, borderwidth=1)
	aktionsfeld = tk.Frame(master=window, borderwidth=1)
	optionsfeld = tk.Frame(master=window, borderwidth=1)
	ereignissfeld.pack()
	aktionsfeld.pack()
	optionsfeld .pack()

	def __init__(self):
		#Legt Anzeigeformat der Stopuhr fest
		self.timestring = "{:02d}:{:02d}:{:02d}".format(0, 0, 0)

	#Befüllt Anzeigenfeld
	def init_ereigniss(self):
		self.ent = tk.Entry(master=self.ereignissfeld, font=("calibri", 18), justify="center", width=6)
		self.label_links = tk.Label(master=self.ereignissfeld, font=("calbri", 24), width=2)
		self.label_rechts = tk.Label(master=self.ereignissfeld, font=("calbri", 24), width=2)
		self.label_links.grid(row=0, column=0, padx=5, pady=7,ipady=12)
		self.ent.grid(row=0, column=1, padx=5, pady=7, ipady=12)
		self.label_rechts.grid(row=0, column=2, padx=5, pady=5) 
	

class Viertes(DreiFenster):
	viertesfeld = tk.Frame(master=window, borderwidth=1)
	viertesfeld.pack()

	def __init__(self,name):
		 self.name = name
		 self.timestring = "{:02d}:{:02d}:{:02d}".format(0, 0, 0)



#window = tk.Tk()
#window.mainloop()