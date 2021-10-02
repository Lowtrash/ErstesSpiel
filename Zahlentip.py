from spielrahmen import DreiFenster
from spielrahmen import window
import tkinter as tk
from stopuhr2 import Stopuhr
from parameter import Paras
import tkinter.messagebox as messagebox

my_para = Paras()
fenetre = DreiFenster()

window.title("Rate die Zahl")

#Befüllt Optionsfeld
def init_optionsfeld():
	global neue_stopuhr
	stopuhr = tk.Label(master=fenetre.optionsfeld, text=fenetre.timestring)
	btn_quit = tk.Button(master=fenetre.optionsfeld, text="QUIT", command=close_all)
	btn_quit.pack(side=tk.LEFT, padx=10)
	btn_info = tk.Button(master=fenetre.optionsfeld, text="NEU")
	btn_info.pack(side=tk.RIGHT, padx=10)
	btn_info['command'] = lambda: restart_game(my_para.geknackt)
	stopuhr.pack(side=tk.RIGHT, padx=45)
	neue_stopuhr = Stopuhr(stopuhr)
	
#Befüllt Spielfeld
def init_spielfeld():
	my_para.geknackt = False
	fenetre.ent.delete(0, tk.END)
	my_para.init_zufall()
	if my_para.eingabe_zähler > 0:
		neue_stopuhr.reset_stopuhr()
		my_para.btn_list = []
	my_para.init_eingabezaehler()
	z = 0
	for i in range(4):
		for j in range(3):
			button = tk.Button(master=fenetre.aktionsfeld, text=my_para.char_list[z], relief=tk.RAISED, font='bold', width=4, height=2, borderwidth=1)
			button['command']=lambda button=button: start_game(button)
			button.grid(row=i, column=j, padx=5, pady=5)
			my_para.btn_list.append(button)
			z +=1
			
#Beendet die Anwendung
def close_all():
	if not neue_stopuhr.timestop:
		window.destroy()
	else:
		neue_stopuhr.stop_stopuhr()
		window.destroy()
	
#Startet das Spiel
def start_game(item):
	delete_clues()
	help = item.cget('text')
	if my_para.eingabe_zähler%2 == 0:
		my_para.werte_erste_eingabe(help)
		if my_para.eingabe_ok:
			if my_para.eingabe_zähler < 1:
				neue_stopuhr.start_stopuhr()
			fenetre.ent.delete(0, tk.END)
			fenetre.ent.insert(int(my_para.eingabe_zähler%2), help)
			my_para.erhöhe_eingabezaehler()
	else:
		my_para.werte_zweite_eingabe(fenetre.ent.get(), item.cget('text'))
		if my_para.eingabe_ok:
			update_game()
			if help != "Enter" and help != "100":
				if int(fenetre.ent.get()) == 100:
					help =""
				fenetre.ent.insert(int(my_para.eingabe_zähler%2), help)
			my_para.erhöhe_eingabezaehler()
			my_para.anzahl_eingaben()
			tip = int(fenetre.ent.get())
			give_clues(tip)

#Mischt das Display
def update_game():
	my_para.mische_buttons()
	ibtn = 0
	for i in range(4):
		for j in range(3):
			button =  my_para.btn_list[ibtn]
			button.grid(row=i, column=j, padx=5, pady=5)
			ibtn += 1

#Zeigt ob Zahl zu gross oder zu klein ist.
#Bei einen Treffer wird dasSpiel neu gestartet
def give_clues(wert):
    if wert < my_para.zufall:
    	fenetre.label_links["text"] = "\u2191"
    	fenetre.label_rechts["text"] = "\u2191"
    elif wert > my_para.zufall:
    	fenetre.label_links["text"] = "\u2193"
    	fenetre.label_rechts["text"] = "\u2193"
    else:
    	my_para.geknackt = True
    	restart_game(my_para.geknackt)

#Löscht Hinweise
def delete_clues():
	fenetre.label_links["text"] = ""
	fenetre.label_rechts["text"] = "" 

#Starte Spiel neu wenn die Zahl errarten wurde,
#oder beim Klicken desNeu Buttons
def restart_game(geknackt):
	global neue_stopuhr
	neue_stopuhr.stop_stopuhr()
	fenetre.label_links["text"] = ""
	fenetre.label_rechts["text"] = ""
	if geknackt:
		info = (int(my_para.eingabe_zähler/2))
		format_string = f"Mit {info} Versuchen"
		messagebox.showinfo("Treffer", format_string)
	help = ""
	fenetre.ent.delete(0, tk.END)
	init_spielfeld()



init_optionsfeld()
fenetre.init_ereigniss()
init_spielfeld()
window.mainloop()