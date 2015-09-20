"""
===========================================================================================
The Predictive
Version 5.1.1 "Dr Octopus"
Console
===========================================================================================
"""

from PR_Launcher import *
from tkinter import *
import sys
import random

info = []
inf = True
try:
	t = open("Smartby_EN.libt" , 'rt')
	#coздaeтcя нoвaя библиoтeкa c нaзвaниeм фaйлa
	Smartby_EN = LIBRARY()
	Smartby_EN.filename = "Smartby_EN.libt"
	Smartby_EN.statistics = {}
	for line in t:
		#пepвыe cтpoки coдepжaт инфopмaцию o библиoтeкe
		if inf:
			#инфopмaция зaпиcывaeтcя в мaccив info
			info.extend(line.split())
			if info[-1] == "info>":
				inf = False
		#пocлe cлeдуeт cтaтиcтикa
		else:
			#oбнoвлeниe cтaтиcтики библиoтeки
			Smartby_EN.statistics.update(eval(line))
	t.close()
	#из мaccивa info инфopмaция coxpaняeтcя в caму библиoтeку
	Smartby_EN.name = info[1]
	Smartby_EN.version = info[2]
	Smartby_EN.reliability = float(info[3])
	Smartby_EN.maxwords = int(info[4])
	if info[5] == "LOCKED":
		Smartby_EN.lock = True
	libraries.append(Smartby_EN)
	settings.library = Smartby_EN
#фaйл библиoтeки нe нaйдeн или нe мoжeт быть пpoчитaн
except IOError or EOFError:
	settings.library = Default

#coздaниe oкнa для вывoдa cлoв нa экpaн
root = Tk()
buttons = []
word = " "
root_text = ""
straw = ""

def predict1(event):
	try:
		global root_text
		global settings
		if not btn1['text'] == ". . .":
			if not list(root_text)[-1] == " ":
				root_text += " "
				window.config(state = 'normal')
				window.insert(END, " ")
				window.config(state = 'disabled')
				sys.stdout.write(" ")
			sys.stdout.write(btn1['text'])
			sys.stdout.write(" ")
			sys.stdout.flush()
		root_text += btn1['text']
		window.config(state = 'normal')
		window.insert(END, btn1['text'])
		root_text += " "
		window.insert(END, " ")
		window.config(state = 'disabled')
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
		wrd4 = ""
		if root_text.split()[-1] in settings.library.statistics:
			wrd1 = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
			try:
				wrd2 = word_output((root_text.split()[-1]) , 2 , settings.library)[1]
			except IndexError:
				wrd2 = "..."
			try:
				wrd3 = word_output((root_text.split()[-1]) , 3 , settings.library)[2]
			except IndexError:
				wrd3 = "..."
			try:
				wrd4 = word_output((root_text.split()[-1]) , 4 , settings.library)[3]
			except IndexError:
				wrd4 = "..."
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
		btn4['text'] = wrd4
	except IndexError or EOFError:
		print("The Predictive widget temporarily inavailable")

def predict2(event):
	try:
		global root_text
		global settings
		if not btn2['text'] == ". . .":
			if not list(root_text)[-1] == " ":
				root_text += " "
				window.config(state = 'normal')
				window.insert(END, " ")
				window.config(state = 'disabled')
				sys.stdout.write(" ")
			sys.stdout.write(btn2['text'])
			sys.stdout.write(" ")
			sys.stdout.flush()
		root_text += btn2['text']
		window.config(state = 'normal')
		window.insert(END, btn2['text'])
		root_text += " "
		window.insert(END, " ")
		window.config(state = 'disabled')
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
		wrd4 = ""
		if root_text.split()[-1] in settings.library.statistics:
			wrd1 = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
			try:
				wrd2 = word_output((root_text.split()[-1]) , 2 , settings.library)[1]
			except IndexError:
				wrd2 = "..."
			try:
				wrd3 = word_output((root_text.split()[-1]) , 3 , settings.library)[2]
			except IndexError:
				wrd3 = "..."
			try:
				wrd4 = word_output((root_text.split()[-1]) , 4 , settings.library)[3]
			except IndexError:
				wrd4 = "..."
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
		btn4['text'] = wrd4
	except IndexError or EOFError:
		print("The Predictive widget temporarily inavailable")

def predict3(event):
	try:
		global root_text
		global settings
		if not btn3['text'] == ". . .":
			if not list(root_text)[-1] == " ":
				root_text += " "
				window.config(state = 'normal')
				window.insert(END, " ")
				window.config(state = 'disabled')
				sys.stdout.write(" ")
			sys.stdout.write(btn3['text'])
			sys.stdout.write(" ")
			sys.stdout.flush()
		root_text += btn3['text']
		window.config(state = 'normal')
		window.insert(END, btn3['text'])
		root_text += " "
		window.insert(END, " ")
		window.config(state = 'disabled')
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
		wrd4 = ""
		if root_text.split()[-1] in settings.library.statistics:
			wrd1 = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
			try:
				wrd2 = word_output((root_text.split()[-1]) , 2 , settings.library)[1]
			except IndexError:
				wrd2 = "..."
			try:
				wrd3 = word_output((root_text.split()[-1]) , 3 , settings.library)[2]
			except IndexError:
				wrd3 = "..."
			try:
				wrd4 = word_output((root_text.split()[-1]) , 4 , settings.library)[3]
			except IndexError:
				wrd4 = "..."
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
		btn4['text'] = wrd4
	except IndexError or EOFError:
		print("The Predictive widget temporarily inavailable")

def predict4(event):
	try:
		global root_text
		global settings
		if not btn4['text'] == ". . .":
			if not list(root_text)[-1] == " ":
				root_text += " "
				window.config(state = 'normal')
				window.insert(END, " ")
				window.config(state = 'disabled')
				sys.stdout.write(" ")
			sys.stdout.write(btn4['text'])
			sys.stdout.write(" ")
			sys.stdout.flush()
		root_text += btn4['text']
		window.config(state = 'normal')
		window.insert(END, btn4['text'])
		root_text += " "
		window.insert(END, " ")
		window.config(state = 'disabled')
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
		wrd4 = ""
		if root_text.split()[-1] in settings.library.statistics:
			wrd1 = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
			try:
				wrd2 = word_output((root_text.split()[-1]) , 2 , settings.library)[1]
			except IndexError:
				wrd2 = "..."
			try:
				wrd3 = word_output((root_text.split()[-1]) , 3 , settings.library)[2]
			except IndexError:
				wrd3 = "..."
			try:
				wrd4 = word_output((root_text.split()[-1]) , 4 , settings.library)[3]
			except IndexError:
				wrd4 = "..."
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
		btn4['text'] = wrd4
	except IndexError or EOFError:
		print("The Predictive widget temporarily inavailable")

def finish1(event):
	try:
		global root_text
		global settings
		if not btn1['text'] == ". . .":
			wr = btn1['text'][len(root_text.split()[-1])::]
			window.config(state = 'normal')
			if wr:
				sys.stdout.write(wr)
				sys.stdout.write(" ")
				sys.stdout.flush()
				root_text += wr
				window.insert(END, wr)
			window.insert(END, " ")
			window.config(state = 'disabled')
			root_text += " "
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
		wrd4 = ""
		if root_text.split()[-1] in settings.library.statistics:
			wrd1 = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
			try:
				wrd2 = word_output((root_text.split()[-1]) , 2 , settings.library)[1]
			except IndexError:
				wrd2 = "..."
			try:
				wrd3 = word_output((root_text.split()[-1]) , 3 , settings.library)[2]
			except IndexError:
				wrd3 = "..."
			try:
				wrd4 = word_output((root_text.split()[-1]) , 4 , settings.library)[3]
			except IndexError:
				wrd4 = "..."
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
		btn4['text'] = wrd4
		btn1.bind("<Button-1>", predict1)
		root.bind("<Alt-KeyPress-1>", predict1)
		btn2.bind("<Button-1>", predict2)
		root.bind("<Alt-KeyPress-2>", predict2)
		btn3.bind("<Button-1>", predict3)
		root.bind("<Alt-KeyPress-3>", predict3)
		btn4.bind("<Button-1>", predict4)
		root.bind("<Alt-KeyPress-4>", predict4)
	except IndexError or EOFError:
		print("The Predictive widget temporarily inavailable")

def finish2(event):
	try:
		global root_text
		global settings
		if not btn2['text'] == ". . .":
			wr = btn2['text'][len(root_text.split()[-1])::]
			window.config(state = 'normal')
			if wr:
				sys.stdout.write(wr)
				sys.stdout.write(" ")
				sys.stdout.flush()
				root_text += wr
				window.insert(END, wr)
			window.insert(END, " ")
			window.config(state = 'disabled')
			root_text += " "
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
		wrd4 = ""
		if root_text.split()[-1] in settings.library.statistics:
			wrd1 = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
			try:
				wrd2 = word_output((root_text.split()[-1]) , 2 , settings.library)[1]
			except IndexError:
				wrd2 = "..."
			try:
				wrd3 = word_output((root_text.split()[-1]) , 3 , settings.library)[2]
			except IndexError:
				wrd3 = "..."
			try:
				wrd4 = word_output((root_text.split()[-1]) , 4 , settings.library)[3]
			except IndexError:
				wrd4 = "..."
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
		btn4['text'] = wrd4
		btn1.bind("<Button-1>", predict1)
		root.bind("<Alt-KeyPress-1>", predict1)
		btn2.bind("<Button-1>", predict2)
		root.bind("<Alt-KeyPress-2>", predict2)
		btn3.bind("<Button-1>", predict3)
		root.bind("<Alt-KeyPress-3>", predict3)
		btn4.bind("<Button-1>", predict4)
		root.bind("<Alt-KeyPress-4>", predict4)
	except IndexError or EOFError:
		print("The Predictive widget temporarily inavailable")

def finish3(event):
	try:
		global root_text
		global settings
		if not btn3['text'] == ". . .":
			wr = btn3['text'][len(root_text.split()[-1])::]
			window.config(state = 'normal')
			if wr:
				sys.stdout.write(wr)
				sys.stdout.write(" ")
				sys.stdout.flush()
				root_text += wr
				window.insert(END, wr)
			window.insert(END, " ")
			window.config(state = 'disabled')
			root_text += " "
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
		wrd4 = ""
		if root_text.split()[-1] in settings.library.statistics:
			wrd1 = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
			try:
				wrd2 = word_output((root_text.split()[-1]) , 2 , settings.library)[1]
			except IndexError:
				wrd2 = "..."
			try:
				wrd3 = word_output((root_text.split()[-1]) , 3 , settings.library)[2]
			except IndexError:
				wrd3 = "..."
			try:
				wrd4 = word_output((root_text.split()[-1]) , 4 , settings.library)[3]
			except IndexError:
				wrd4 = "..."
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
		btn4['text'] = wrd4
		btn1.bind("<Button-1>", predict1)
		root.bind("<Alt-KeyPress-1>", predict1)
		btn2.bind("<Button-1>", predict2)
		root.bind("<Alt-KeyPress-2>", predict2)
		btn3.bind("<Button-1>", predict3)
		root.bind("<Alt-KeyPress-3>", predict3)
		btn4.bind("<Button-1>", predict4)
		root.bind("<Alt-KeyPress-4>", predict4)
	except IndexError or EOFError:
		print("The Predictive widget temporarily inavailable")

def finish4(event):
	try:
		global root_text
		global settings
		if not btn4['text'] == ". . .":
			wr = btn4['text'][len(root_text.split()[-1])::]
			window.config(state = 'normal')
			if wr:
				sys.stdout.write(wr)
				sys.stdout.write(" ")
				sys.stdout.flush()
				root_text += wr
				window.insert(END, wr)
			window.insert(END, " ")
			window.config(state = 'disabled')
			root_text += " "
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
		wrd4 = ""
		if root_text.split()[-1] in settings.library.statistics:
			wrd1 = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
			try:
				wrd2 = word_output((root_text.split()[-1]) , 2 , settings.library)[1]
			except IndexError:
				wrd2 = "..."
			try:
				wrd3 = word_output((root_text.split()[-1]) , 3 , settings.library)[2]
			except IndexError:
				wrd3 = "..."
			try:
				wrd4 = word_output((root_text.split()[-1]) , 4 , settings.library)[3]
			except IndexError:
				wrd4 = "..."
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
		btn4['text'] = wrd4
		btn1.bind("<Button-1>", predict1)
		root.bind("<Alt-KeyPress-1>", predict1)
		btn2.bind("<Button-1>", predict2)
		root.bind("<Alt-KeyPress-2>", predict2)
		btn3.bind("<Button-1>", predict3)
		root.bind("<Alt-KeyPress-3>", predict3)
		btn4.bind("<Button-1>", predict4)
		root.bind("<Alt-KeyPress-4>", predict4)
	except IndexError or EOFError:
		print("The Predictive widget temporarily inavailable")

def select(event):
	global libraries
	global settings
	global root
	for i in range(len(libraries)):
		if libraries[i].name == settings.library.name:
			now = i
	if not now+1 == len(libraries):
		settings.library = libraries[now+1]
	else:
		settings.library = libraries[0]
	btnlib['text'] = settings.library.name

def save(event):
	global root
	global root_text
	root.clipboard_clear()
	root.clipboard_append(window.get('1.0', 'end'))

btn1 = Button(root, text = ". . .", width = 29, height = 1, bg = "floral white", fg = "NavajoWhite4")
btn1.bind("<Button-1>", finish1)
root.bind("<Alt-1>", finish1)
btn1.grid(row = 1, column = 1, columnspan = 26)

btn2 = Button(root, text = "...", width = 21, height = 1, bg = "floral white", fg = "NavajoWhite4")
btn2.bind("<Button-1>", finish2)
root.bind("<Alt-2>", finish2)
btn2.grid(row = 2, column = 0, columnspan = 20)

btn3 = Button(root, text = "...", width = 14, height = 1, bg = "floral white", fg = "NavajoWhite4")
btn3.bind("<Button-1>", finish3)
root.bind("<Alt-3>", finish3)
btn3.grid(row = 2, column = 20, columnspan = 14)

btn4 = Button(root, text = "...", width = 14, height = 1, bg = "floral white", fg = "NavajoWhite4")
btn4.bind("<Button-1>", finish4)
root.bind("<Alt-4>", finish4)
btn4.grid(row = 2, column = 34, columnspan = 14)

btncls = Button(root, text = "Save", width = 7, height = 1, bg = "burlywood3", fg = "gray12")
btncls.bind("<Button-1>", save)
root.bind("<Alt-s>", save)
btncls.grid(row = 1, column = 40, columnspan = 7)

btnlib = Button(root, text = settings.library.name, width = 13, height = 1, bg = "lemon chiffon", fg = "gray12")
btnlib.bind("<Button-1>", select)
root.bind("<Control-F4>", select)
btnlib.grid(row = 1, column = 27, columnspan = 13)

scroll = Scrollbar(root)
window = Text(root, height = 4, width = 40)
scroll.grid(row = 3, column = 43, columnspan = 3)
window.grid(row = 3, column = 1, columnspan = 40)
scroll.config(command = window.yview)
window.config(yscrollcommand = scroll.set)
window.config(state = 'disabled')

def finish(straw):
	global settings
	stats = settings.library.statistics
	varts = []
	best = [("", 0)]*4
	for word in stats:
		if straw == word[:(len(straw))]:
			cor = 0
			for poss in stats[word]:
				cor += stats[word][poss]
			varts.append((word, cor))
	if len(varts):
		best = [(varts[0][0], 0)] * 4
		for trial in varts:
			if trial[1] > best[0][1]:
				best[0] = trial
			elif trial[1] > best[1][1] and not trial[1] > best[0][1]:
				best[1] = trial
			elif trial[1] > best[2][1] and not trial[1] > best[1][1]:
				best[2] = trial
			elif trial[1] > best[3][1] and not trial[1] > best[2][1]:
				best[3] = trial
	return([best[0][0], best[1][0], best[2][0], best[3][0]])

def wrkey(event):
	global root
	global root_text
	global straw
	if event.keysym == 'Escape':
		root.clipboard_clear()
		root.clipboard_append(window.get('1.0', 'end'))
		root_text += "\n"
		window.config(state = 'normal')
		window.insert(END, "\n")
		window.config(state = 'disabled')
		print("\nText copied to clipboard, use Ctrl+V to paste it later.")
	elif event.keysym == 'BackSpace':
		root_text = root_text[:-1]
		window.config(state = 'normal')
		window.delete('end-2c')
		window.config(state = 'disabled')
	elif event.keysym == 'Return':
		print("")
		root_text += "\n"
		window.config(state = 'normal')
		window.insert(END, "\n")
		window.config(state = 'disabled')
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
		wrd4 = ""
		if root_text.split()[-1] in settings.library.statistics:
			wrd1 = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
			try:
				wrd2 = word_output((root_text.split()[-1]) , 2 , settings.library)[1]
			except IndexError:
				wrd2 = "..."
			try:
				wrd3 = word_output((root_text.split()[-1]) , 3 , settings.library)[2]
			except IndexError:
				wrd3 = "..."
			try:
				wrd4 = word_output((root_text.split()[-1]) , 4 , settings.library)[3]
			except IndexError:
				wrd4 = "..."
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
		btn4['text'] = wrd4
	elif event.char in {".", "?", "!", ",", ";", ":", "'"}:
		x = event.char
		sys.stdout.write(x)
		if list(root_text)[-1] == " ":
			root_text = root_text[:-1]+str(x)
			window.config(state = 'normal')
			window.delete('end-2c')
			window.config(state = 'disabled')
		window.config(state = 'normal')
		window.insert(END, x)
		window.config(state = 'disabled')
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
		wrd4 = ""
		if root_text.split()[-1] in settings.library.statistics:
			wrd1 = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
			try:
				wrd2 = word_output((root_text.split()[-1]) , 2 , settings.library)[1]
			except IndexError:
				wrd2 = "..."
			try:
				wrd3 = word_output((root_text.split()[-1]) , 3 , settings.library)[2]
			except IndexError:
				wrd3 = "..."
			try:
				wrd4 = word_output((root_text.split()[-1]) , 4 , settings.library)[3]
			except IndexError:
				wrd4 = "..."
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
		btn4['text'] = wrd4
		sys.stdout.flush()
	else:
		x = event.char
		sys.stdout.write(x)
		root_text += str(x)
		window.config(state = 'normal')
		window.insert(END, x)
		window.config(state = 'disabled')
		if len(root_text):
			if list(root_text)[-1] == " ":
				wrd1 = ". . ."
				wrd2 = ""
				wrd3 = ""
				wrd4 = ""
				if root_text.split()[-1] in settings.library.statistics:
					wrd1 = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
					try:
						wrd2 = word_output((root_text.split()[-1]) , 2 , settings.library)[1]
					except IndexError:
						wrd2 = "..."
					try:
						wrd3 = word_output((root_text.split()[-1]) , 3 , settings.library)[2]
					except IndexError:
						wrd3 = "..."
					try:
						wrd4 = word_output((root_text.split()[-1]) , 4 , settings.library)[3]
					except IndexError:
						wrd4 = "..."
				btn1['text'] = wrd1
				btn2['text'] = wrd2
				btn3['text'] = wrd3
				btn4['text'] = wrd4
				btn1.bind("<Button-1>", predict1)
				root.bind("<Alt-KeyPress-1>", predict1)
				btn2.bind("<Button-1>", predict2)
				root.bind("<Alt-KeyPress-2>", predict2)
				btn3.bind("<Button-1>", predict3)
				root.bind("<Alt-KeyPress-3>", predict3)
				btn4.bind("<Button-1>", predict4)
				root.bind("<Alt-KeyPress-4>", predict4)
			else:
				wrds = finish(root_text.split()[-1])
				wrd1 = wrds[0]
				wrd2 = wrds[1]
				wrd3 = wrds[2]
				wrd4 = wrds[3]
				btn1['text'] = wrd1
				btn2['text'] = wrd2
				btn3['text'] = wrd3
				btn4['text'] = wrd4
				btn1.bind("<Button-1>", finish1)
				root.bind("<Alt-KeyPress-1>", finish1)
				btn2.bind("<Button-1>", finish2)
				root.bind("<Alt-KeyPress-2>", finish2)
				btn3.bind("<Button-1>", finish3)
				root.bind("<Alt-KeyPress-3>", finish3)
				btn4.bind("<Button-1>", finish4)
				root.bind("<Alt-KeyPress-4>", finish4)
		sys.stdout.flush()

def wrmode():
	global root
	global wrkey
	root.bind_all('<Key>', wrkey)
	return(0)

print("Type 'write' to enter writing mode with 'The Predictive' or type 'launch' to enter launcher mode.")
print("Type 'exit' or 'quit' to stop this programm.")

command = "write"
end = 0
while not end:
	if command == "write":
		print("Press 'Esc' to save current text.")
		print("Open the Tkinter window to begin.")
		print("write >>>\n")
		wrmode()
	elif command in {"start", "launch", "settings"}:
		launch()
	elif command in {"quit", "exit"}:
		end = 1
	print("start >>>\n")
	command = input()

root.mainloop()
