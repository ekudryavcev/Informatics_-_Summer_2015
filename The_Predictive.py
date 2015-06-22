"""
===========================================================================================
The Predictive
Version 3.1.1 "Dr Seuss"
Console
===========================================================================================
"""

from PR_Launcher import *
from tkinter import *
import sys
import random

#coздaниe oкнa для вывoдa cлoв нa экpaн
root = Tk()
buttons = []
word = " "
root_text = ""

def clicked(event):
	global root_text
	global settings
	if not btn['text'] == ". . .":
		if not root_text[-1] == " ":
			root_text += " "
			sys.stdout.write(" ")
		sys.stdout.write(btn['text'])
		sys.stdout.write(" ")
		sys.stdout.flush()
	wrd = ""
	if root_text.split()[-1] in settings.library.statistics:
		wrd = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
	root_text += wrd
	root_text += " "
	if root_text.split()[-1] in settings.library.statistics:
		wrd = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
	btn['text'] = wrd

btn = Button(root, text = ". . .", width = 10, height = 3, bg = "floral white", fg = "NavajoWhite4")
btn.bind("<Button-1>", clicked)
btn.grid(row = 1, column = 1, columnspan = 2)

def wrkey(event):
	global root
	global root_text
	if event.keysym == 'Escape':
		root.clipboard_clear()
		root.clipboard_append(root_text)
		#root.destroy()
	elif event.keysym == 'Return':
		print("")
		root_text += "\n"
		wrd = ""
		if root_text.split()[-1] in settings.library.statistics:
			wrd = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
		btn['text'] = wrd
	elif event.keysym == ".":
		x = event.char
		sys.stdout.write(x)
		if root_text[-1] == " ":
			root_text[-1] = str(x)
			wrd = ""
			if root_text.split()[-1] in settings.library.statistics:
				wrd = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
			btn['text'] = wrd
		sys.stdout.flush()
	else:
		x = event.char
		sys.stdout.write(x)
		root_text += str(x)
		if root_text[-1] == " ":
			wrd = ""
			if root_text.split()[-1] in settings.library.statistics:
				wrd = word_output((root_text.split()[-1]) , 1 , settings.library)[0]
			btn['text'] = wrd
		sys.stdout.flush()

def wrmode():
	global root
	global wrkey
	root.bind_all('<Key>', wrkey)
	return(0)

print("Type 'write' to enter writing mode with 'The Predictive' or type 'launch' to enter launcher mode.")
print("Type 'exit' or 'quit' to stop this programm.")

end = 0
while not end:
	print("start >>>\n")
	command = input()
	if command == "write":
		print("Press 'Esc' to quit this mode.")
		print("Open the Tkinter window to begin.")
		print("write >>>\n")
		wrmode()
		end = 1
	elif command in {"start", "launch", "settings"}:
		launch()
	elif command in {"quit", "exit"}:
		end = 1

root.mainloop()
print("Text copied to clipboard, use Ctrl+V to paste it later.")
