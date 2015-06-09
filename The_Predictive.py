"""
The Predictive
Version 1.1.5 Dr Zero
Settings launcher for working with libraries
"""

class SETTINGS:
	name = "Default"
	library = None
	autodidact = True

class LIBRARY:
	name = "Default"
	filename = "default.txt"
	version = "1.1.5"
	reliability = 0.0
	maxwords = 1
	lock = False

def file_restore(lib):
	global libraries
	global version
	lib.filename = lib.name + ".libt"
	l = open(lib.filename , 'w')
	lock = ""
	if lib.lock == True:
		lock = "LOCKED"
	l.write("<info" + "\n" + lib.name + "\n" + lib.version + "\n" + str(lib.reliability) + "\n" + str(lib.maxwords) + "\n" + lock + "\ninfo>\n")
	l.close()

version = "1.1.5"
all_vers = ["1.0.2" , "1.0.3" , "1.1.1" , "1.1.3" , "1.1.4" , "1.1.5" , "1.2.beta"]
lib_def = LIBRARY()
libraries = [lib_def]
file_restore(lib_def)
set_def = SETTINGS()
set_def.library = lib_def
settings = set_def

commands_info = {"'help'" : "list of commands" , "'info'" : "current settings information" , "'new_lib'" : "create a new statistics library" , "'libraries'" : "list of existing statistics libraries" , "'change_lib'" : "change current statistics library" , "finish" : "stop this console" , "stop_console" : "stop this console" , "close_dialogue" : "stop this console"}
print("Input command")
print("Type 'help' to see possible commands or 'info' to see current settings.")


def new_lib_dialog():
	print("Type the name of the new statistics library")
	comnd = input()
	global settings
	global libraries
	global LIBRARY
	global version
	exists = False
	for lib in libraries:
		if lib.name == comnd:
			exists = True
	if exists:
		print("There already exists a library with this name.")
		return(new_lib_dialog())
	else:
		new_lib = LIBRARY()
		new_lib.name = comnd
		print("Would you like to apply special changes to the new library?")
		if yes_no(input()):
			print("You may change the version by typing 'version', maximum words with 'maxwords' and lock with 'lock'. Type 'finish' to leave this mode.")
			comnd = input()
			while not comnd == "finish":
				if comnd == "version":
					print("You may choose one of the following versions:")
					print(all_vers)
					print("Current version is " + version)
					print("Customizing versions of the libraries is not recommended.")
					comnd = input()
					if comnd in all_vers:
						new_lib.version = comnd
						print("The library version is successfully changed.")
					else:
						print("Such version is inavailable.")
				elif comnd == "maxwords":
					print("Input the maximum ammount of words to be analysed.")
					new_lib.maxwords = max(1 , min(7 , int(input())))
					print("The maximum ammount of words is successfully changed.")
				elif comnd == "lock":
					print("Would you like to lock the library so that its statistics didn't change?")
					if yes_no(input()):
						new_lib.lock = True
						print("The library is now locked.")
					else:
						new_lib.lock = False
						print("The library is now unlocked.")
				else:
					print("There is no similar command. It may appear in the following versions.")
				comnd = input()
			file_restore(new_lib)
			libraries.append(new_lib)
			print("A new library called '" + new_lib.name + "' is successfuly saved.")

def yes_no(ansr):
	yep = {"Yes" , "YES" , "yes" , "Y" , "y" , "Yep" , "yep" , "YEP" , "Yeah" , "yeah" , "YEAH" , "Sure" , "SURE" , "sure"}
	nope = {"No" , "NO" , "no" , "N" , "n" , "Nope" , "nope" , "NOPE" , "Noah" , "noah" , "NOAH"}
	if ansr in yep:
		return(1)
	elif ansr in nope:
		return(0)
	else:
		print("You should answer in a way, similar to 'Yes'/'No'.")
		return(yes_no(input()))

"""
STARTS HERE:
"""

def start(command): 
	global settings
	global commands_info
	global libraries
	global LIBRARY
	global new_lib_dialog
	global yes_no

	if command == "help" or command == "Help":
		print("Here is the list of available commands:")
		for c in commands_info:
			print(c , "-" , commands_info[c])

	elif command == "info" or command == "Info":
		print("Here is the information about current settings:")
		print(settings.name)
		print("Statistics library:" , settings.library.name)
		print("Statistics reliability:" , str(settings.library.reliability * 100) + "%")
		print("Machine learning mode:" , settings.autodidact)

	elif command == "change_lib":
		print("Input the name of the statistics library or 'libraries' to see the list of libraries.")
		comnd = input()
		key = 1
		if comnd == "libraries":
			if libraries == None:
				print("No libraries yet, but you can create one now.")
				key = 0
			else:
				print("Here is the list of existing statistics libraries:")
				for lib in libraries:
					print(lib.name)
				print("Which library would you use?")
				comnd = input()
				key = 1
		if key:
			exists = False
			for lib in libraries:
				if lib.name == comnd:
					key = 0
					if not version == lib.version:
						print("The library version is " + str(lib.version) + ", which is lower than current " + str(version) + ".")
						key = 1
					if lib.reliability<0.25 and key==0:
						print("The rate of this library is " + str(lib.reliability) + ", which is quite low.")
						key = 1
					elif lib.reliability<0.25:
						print("Also, the rate of this library is " + str(lib.reliability) + ", which is quite low.")
						print("So this statistics library has a low reliability.")
					if key:
						print("Are you sure you would like to proceed?")
						if yes_no(input()):
							settings.library = lib
							exists = True
						else:
							print("You may choose another library from the 'libraries' list.")
							return(0)
					else:
						settings.library = lib
						exists = True
			if exists:
				print("The changes are applied, you may type 'info' to check them.")
			else:
				print("No library with such name found, but you can create one now.")

	elif command == "new_lib":
		new_lib_dialog()
		print("Would you like to use this library now?")
		a = yes_no(input())
		if a:
			settings.library = libraries[-1]
			print("The changes are applied, you may type 'info' to check them.")
		else:
			print("You may apply it later by typing 'change_lib'.")

	elif command == "libraries":
		if len(libraries):
			print("Here is the list of existing statistics libraries:")
			for lib in libraries:
				print(lib.name)
		else:
			print("No libraries yet, but you can create one now")

	elif command in {"stop_console" , "close_dialogue" , "finish"}:
		return(1)

	else:
		print("There is no similar command. It may appear in the following versions.")
		print("You may type 'help' to see possible commands.")
		return(start(input()))

	return(0)

end = 0
while not end:
	end = start(input())
