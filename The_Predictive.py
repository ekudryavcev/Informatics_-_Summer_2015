"""
===========================================================================================
The Predictive
Version 3.1.3 "Dr Seuss"
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

def clicked1(event):
	try:
		global root_text
		global settings
		if not btn1['text'] == ". . .":
			if not list(root_text)[-1] == " ":
				root_text += " "
				sys.stdout.write(" ")
			sys.stdout.write(btn1['text'])
			sys.stdout.write(" ")
			sys.stdout.flush()
		root_text += btn1['text']
		root_text += " "
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
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
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
	except IndexError or EOFError:
		print("The Predictive widget temporarily inavailable")

def clicked2(event):
	try:
		global root_text
		global settings
		if not btn2['text'] == ". . .":
			if not list(root_text)[-1] == " ":
				root_text += " "
				sys.stdout.write(" ")
			sys.stdout.write(btn2['text'])
			sys.stdout.write(" ")
			sys.stdout.flush()
		root_text += btn2['text']
		root_text += " "
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
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
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
	except IndexError or EOFError:
		print("The Predictive widget temporarily inavailable")

def clicked3(event):
	try:
		global root_text
		global settings
		if not btn3['text'] == ". . .":
			if not list(root_text)[-1] == " ":
				root_text += " "
				sys.stdout.write(" ")
			sys.stdout.write(btn3['text'])
			sys.stdout.write(" ")
			sys.stdout.flush()
		root_text += btn3['text']
		root_text += " "
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
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
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
	except IndexError or EOFError:
		print("The Predictive widget temporarily inavailable")

btn1 = Button(root, text = ". . .", width = 13, height = 3, bg = "floral white", fg = "NavajoWhite4")
btn1.bind("<Button-1>", clicked1)
btn1.grid(row = 1, column = 1, columnspan = 2)

btn2 = Button(root, text = "...", width = 6, height = 2, bg = "floral white", fg = "NavajoWhite4")
btn2.bind("<Button-1>", clicked2)
btn2.grid(row = 2, column = 1)

btn3 = Button(root, text = "...", width = 6, height = 2, bg = "floral white", fg = "NavajoWhite4")
btn3.bind("<Button-1>", clicked3)
btn3.grid(row = 2, column = 2)

def wrkey(event):
	global root
	global root_text
	if event.keysym == 'Escape':
		root.clipboard_clear()
		root.clipboard_append(root_text)
		print("Text copied to clipboard, use Ctrl+V to paste it later.")
	elif event.keysym == 'Return':
		print("")
		root_text += "\n"
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
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
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
	elif event.char in {".", "?", "!", ",", ";", ":", "'"}:
		x = event.char
		sys.stdout.write(x)
		if list(root_text)[-1] == " ":
			root_text = root_text[:-1]+str(x)
		wrd1 = ". . ."
		wrd2 = ""
		wrd3 = ""
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
		btn1['text'] = wrd1
		btn2['text'] = wrd2
		btn3['text'] = wrd3
		sys.stdout.flush()
	else:
		x = event.char
		sys.stdout.write(x)
		root_text += str(x)
		if len(root_text):
			if list(root_text)[-1] == " ":
				wrd1 = ". . ."
				wrd2 = ""
				wrd3 = ""
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
				btn1['text'] = wrd1
				btn2['text'] = wrd2
				btn3['text'] = wrd3
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
		print("Press 'Esc' to save current text.")
		print("Open the Tkinter window to begin.")
		print("write >>>\n")
		wrmode()
		end = 1
	elif command in {"start", "launch", "settings"}:
		launch()
	elif command in {"quit", "exit"}:
		end = 1

root.mainloop()
