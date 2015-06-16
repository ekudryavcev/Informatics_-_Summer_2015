"""
========================================================================================================================================
The Predictive
Version 2.0.1 "Dr Ulysses"
Settings launcher for working with libraries
========================================================================================================================================
"""

#объект класса настроек
class SETTINGS:
	name = "Default"
	library = None
	autodidact = True
	showwords = 5


#объект класса библиотек
class LIBRARY:
	name = "Default"
	filename = "default.txt"
	statistics = {}
	version = "2.0.1"
	reliability = 0.0
	maxwords = 1
	lock = False

#создание файла фомата *.libt для хранения библиотеки
def restore_file(lib):
	global version
	lib.filename = lib.name + ".libt"
	l = open(lib.filename , 'w')
	lock = ""
	if lib.lock == True:
		lock = "LOCKED"
	#информация о библиотеке
	l.write("<info" + "\n" + lib.name + "\n" + lib.version + "\n" + str(lib.reliability) + "\n" + str(lib.maxwords) + "\n" + lock + "\ninfo>")
	l.write("\n" + str(lib.statistics))
	l.close()

#создание настроек и библиотек по умолчанию
version = "2.0.1"
all_vers = ["1.0.2","1.0.3","1.1.1","1.1.3","1.1.4","1.1.5","1.1.6","1.2.0","1.2.2","1.2.4","1.3.0","1.3.1","1.3.3","1.3.4","1.3.5","1.4.0","2.0.1","2.0.0.beta"]
lib_def = LIBRARY()
libraries = [lib_def]
restore_file(lib_def)
set_def = SETTINGS()
set_def.library = lib_def
settings = set_def
builtin_libs = ["Smartby_EN" , "Keyloot_EN" , "Queru_EN" , "Walret_PY"]

#список команд с пояснениями
commands_info = {"'help'" : "list of commands" , "'info'" : "current settings information" , "'new_lib'" : "create a new statistics library"}
commands_info.update({"'libraries'" : "list of existing statistics libraries" , "'change_lib'" : "change current statistics library"})
commands_info.update({"'quit'" : "return back" , "'stop_console', 'close_dialogue'" : "stop this console" , "'edit_settings', 'edit_sets'" : "edit current settings"})
commands_info.update({"'new_adid'" : "create a new empty *.adid training file" , "'edit_lib'" : "edit statistics library parameters"})
commands_info.update({"'run_text'" : "run machine learning on a certain text" , "'restore_lib'" : "restore a library from a statistics file"})
commands_info.update({"'restore_def'" : "restore all built-in libraries"})

#создание окна для вывода слов на экран
from tkinter import *
root = Tk()
buttons = []
word = " "

#функция для создания пользователем новой библиотеки
def new_lib_dialog():
	print("Type the name of the new statistics library")
	print("new_lib >>>\n")
	comnd = input()
	global settings
	global libraries
	global LIBRARY
	global version
	global all_vers
	exists = False
	#если имя уже занято другой библиотекой, предлагается выбрать другое имя
	for lib in libraries:
		if lib.name == comnd:
			print("There already exists a library with this name.")
			return(new_lib_dialog())
	else:
		#создается пустая библиотека с пользовательским именем
		new_lib = LIBRARY()
		new_lib.name = comnd
		print("Would you like to apply special changes to the new library?")
		print("new_lib >>>\n")
		#режим редактирования новой библиотеки
		if yes_no(input()):
			print("You may change the version by typing 'version', maximum words with 'maxwords' and lock with 'lock'. Type 'quit' to leave this mode.")
			print("new_lib >>>\n")
			comnd = input()
			while not comnd == "quit":
				#изменение версии библиотеки - более старые версии могут хранить статистику не так, как новые
				if comnd == "version":
					print("You may choose one of the following versions:")
					print(all_vers)
					print("Current version is " + version)
					print("Customizing versions of the libraries is not recommended.")
					print("new_lib >>>\n")
					comnd = input()
					if comnd in all_vers:
						new_lib.version = comnd
						print("The library version is successfully changed.")
					else:
						print("Such version is inavailable.")
				#изменение максимального количества последних слов, по которым ведется статистика
				elif comnd == "maxwords":
					print("Input the maximum ammount of words to be analysed.")
					print("new_lib >>>\n")
					new_lib.maxwords = max(1 , min(7 , int(input())))
					print("The maximum ammount of words is successfully changed.")
				#блокирование библиотеки с тем чтобы она не изменялась в процессе самообучения
				elif comnd == "lock":
					print("Would you like to lock the library so that its statistics didn't change?")
					print("yes_no >>>\n")
					if yes_no(input()):
						new_lib.lock = True
						print("The library is now locked.")
					else:
						new_lib.lock = False
						print("The library is now unlocked.")
				else:
					print("There is no similar command. It may appear in the following versions.")
				print("new_lib >>>\n")
				comnd = input()
		#создание нового файла со статистикой
		restore_file(new_lib)
		libraries.append(new_lib)
		print("A new library called '" + new_lib.name + "' is successfuly saved.")
		return(new_lib)

#функция, распознающая ответ пользователя
def yes_no(ansr):
	#утвердительный ответ
	yep = {"Yes" , "YES" , "yes" , "Y" , "y" , "Yep" , "yep" , "YEP" , "Yeah" , "yeah" , "Ye" , "YE" , "ye" , "YEAH" , "Sure" , "SURE" , "sure"}
	#отрицательный ответ
	nope = {"No" , "NO" , "no" , "N" , "n" , "Nope" , "nope" , "NOPE" , "Noah" , "noah" , "NOAH"}
	if ansr in yep:
		return(1)
	elif ansr in nope:
		return(0)
	else:
		print("You should answer in a way, similar to 'Yes'/'No'.")
		print("yes_no >>>\n")
		return(yes_no(input()))


"""
========================================================================================================================================
STARTS HERE:
========================================================================================================================================
"""

#изменение настроек
def edit_sets():
	global libraries
	global yes_no
	global settings
	print("You may change the library by typing 'change_lib', words showed on the bar with 'show_words' and autodidaction with 'lock'. Type 'save' or 'quit' to leave this mode; type 'info' to see current settings.")
	print("edit_sets >>>\n")
	comnd = input()
	while not comnd in {"quit" , "save"}:
		#изменение количества слов в окне
		if comnd == "show_words":
			print("Input the ammount of words to be offered on the bar.")
			print("edit_sets >>>\n")
			try:
				settings.showwords = max(1 , min(7 , int(input())))
				print("The ammount of words is successfully changed.")
			except:
				print("Inappropriate input.")
		#выключение режима самообучения с тем чтобы библиотеки не изменялись
		elif comnd == "lock":
			print("Would you like to lock autodidaction so that the statistics didn't change?")
			print("yes_no >>>\n")
			if yes_no(input()):
				settings.autodidact = False
				print("Machine learning is now locked.")
			else:
				settings.autodidact = True
				print("Machine learning is now unlocked.")
		#информация о текущих настройках
		elif comnd == "info":
			print("Here is the information about current settings:")
			print(settings.name)
			print("Statistics library:" , settings.library.name)
			print("Statistics reliability:" , str(int(settings.library.reliability * 10000) / 100) + "%")
			print("Words offered:" , str(settings.showwords))
			print("Machine learning mode:" , settings.autodidact)
		#смена библиотеки - см далее
		elif comnd == "change_lib":
				change_lib()
		else:
			print("There is no similar command. It may appear in the following versions.")
		print("edit_sets >>>\n")
		comnd = input()

#редактирование библиотеки
def edit_lib():
	global libraries
	global yes_no
	global all_vers
	print("Input the name of the statistics library or 'libraries' to see the list of libraries.")
	print("edit_lib >>>\n")
	comnd = input()
	key = 1
	#список всех доступных библиотек
	if comnd == "libraries":
		if libraries == None:
			print("No libraries yet, but you can create one now.")
			key = 0
		else:
			print("Here is the list of existing statistics libraries:")
			for lib in libraries:
				print(lib.name)
			print("Which library would you like to edit?")
			print("edit_lib >>>\n")
			comnd = input()
			key = 1
	exists = False
	if key:
		#проверка названия
		for libr in libraries:
			if libr.name == comnd:
				print("You may change the version by typing 'version', maximum words with 'maxwords' and lock with 'lock'. Type 'save' or 'quit' to leave this mode.")
				print("edit_lib >>>\n")
				comnd = input()
				while not comnd in {"quit" , "save"}:
					#изменение версии библиотеки - более старые версии могут хранить статистику не так, как новые
					if comnd == "version":
						print("You may choose one of the following versions:")
						print(all_vers)
						print("Current version is " + version)
						print("Customizing versions of the libraries is not recommended.")
						print("edit_lib >>>\n")
						comnd = input()
						if comnd in all_vers:
							libr.version = comnd
							print("The library version is successfully changed.")
						else:
							print("Such version is inavailable.")
					#изменение максимального количества последних слов, по которым ведется статистика
					elif comnd == "maxwords":
						print("Input the maximum ammount of last words to be analysed.")
						print("edit_lib >>>\n")
						libr.maxwords = max(1 , min(7 , int(input())))
						print("The maximum ammount of words is successfully changed.")
					#блокирование библиотеки с тем чтобы она не изменялась в процессе самообучения
					elif comnd == "lock":
						print("Would you like to lock the library so that its statistics didn't change?")
						print("yes_no >>>\n")
						if yes_no(input()):
							libr.lock = True
							print("The library is now locked.")
						else:
							libr.lock = False
							print("The library is now unlocked.")
					else:
						print("There is no similar command. It may appear in the following versions.")
					print("edit_lib >>>\n")
					comnd = input()
				#обновление файла библиотеки
				restore_file(libr)
			exists = True
	if not exists:
		print("No library with such name found.")

#смена действующей библиотеки
def change_lib():
	global settings
	global libraries
	global yes_no
	print("Input the name of the statistics library or 'libraries' to see the list of libraries.")
	print("change_lib >>>\n")
	comnd = input()
	key = 1
	#список всех доступных библиотек
	if comnd == "libraries":
		if libraries == None:
			print("No libraries yet, but you can create one now.")
			key = 0
		else:
			print("Here is the list of existing statistics libraries:")
			for lib in libraries:
				print(lib.name)
			print("Which library would you use?")
			print("change_lib >>>\n")
			comnd = input()
			key = 1
	if key:
		exists = False
		#проверка названия
		for lib in libraries:
			if lib.name == comnd:
				key = 0
				#нерекомендованные библиотеки
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
					print("yes_no >>>\n")
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
			#изменение действующей библиотеки в настройках
			if settings.library.lock:
				settings.autodidact = False
			print("The changes are applied, you may type 'info' to check them.")
		else:
			print("No library with such name found, but you can create one now.")

#команда создания новой библиотеки
def new_lib():
	global settings
	global libraries
	global LIBRARY
	global new_lib_dialog
	global yes_no
	#использование функции new_lib_dialog
	libraries.append(new_lib_dialog())
	print("Would you like to use this library now?")
	print("yes_no >>>\n")
	a = yes_no(input())
	if a:
		settings.library = libraries[-1]
		print("The changes are applied, you may type 'info' to check them.")
	else:
		print("You may apply it later by typing 'change_lib'.")

#функция самообучения на текстовом файле
def run_text():
	global settings
	global libraries
	global LIBRARY
	global didaction
	global yes_no
	#библиотека и самообучение должны быть разблокированы
	if settings.autodidact:
		print("Which library would you like to edit? Current library is " + settings.library.name + ". Type 'libraries' for the list of all libraries.")
		print("run_text >>>\n")
		comnd = input()
		key = 1
		#пользователь сам выбирает библиотеку для самообучения
		if comnd == "libraries":
			if libraries == None:
				print("No libraries yet, but you can create one now.")
				key = 0
			else:
				print("Here is the list of existing statistics libraries:")
				for lib in libraries:
					print(lib.name)
				print("Which library would you use?")
				print("run_text >>>\n")
				comnd = input()
				key = 1
		if not settings.library.lock:
			if key:
				exists = False
				for lib in libraries:
					if lib.name == comnd:
						if not version == lib.version:
							#нерекомендованные библиотеки
							print("The library version is " + str(lib.version) + ", which is lower than current " + str(version) + ".")
							print("Are you sure you would like to proceed?")
							print("yes_no >>>\n")
							if yes_no(input()):
								libr = lib
								exists = True
							else:
								print("You may apply machine learning later. Now you will return home.")
								return(0)
						else:
							libr = lib
							exists = True
				if exists:
					#поиск файла формата *.adid или *.txt
					print("Input the name of the *.txt or *.adid file. Example: 'Great_Gatsby.txt' . NB: the file should be in the same directory as the app.")
					print("run_text >>>\n")
					filename = input()
					#массив слов файла
					didact = []
					try:
						t = open(filename , 'rt')
						for line in t:
							didact.extend(line.split())
						t.close()
						#применение функции записи статистики - см далее
						didaction(didact , libr)
						restore_file(libr)
						print("The " + libr.name + " library is successfully updated.")
					#файл не найден или не может быть прочитан
					except IOError or EOFError:
						print("There is no appropriate file with such name in the directory. You now will return home.")
				else:
					print("No library with such name found, but you can create one now. You will return home.")
		else:
			print("Machine learning is currently locked. Try to enable autodidaction or change the library.")
	else:
		print("Machine learning is currently locked. Try to enable autodidaction or change the library.")

#команда восстановления библиотеки из файла *.libt
def restore_lib():
	global settings
	global libraries
	global LIBRARY
	global yes_no
	print("Input the name of the *.libt file. Example: 'Queru.libt'. NB: the file should be in the same directory as the app.")
	print("restore_lib >>>\n")
	filename = input()
	info = []
	inf = True
	print(filename + " unpacking...")
	try:
		t = open(filename , 'rt')
		#создается новая библиотека с названием файла
		new_lib = LIBRARY()
		new_lib.filename = filename
		new_lib.statistics = {}
		for line in t:
			#первые строки содержат информацию о библиотеке
			if inf:
				#информация записывается в массив info
				info.extend(line.split())
				if info[-1] == "info>":
					inf = False
			#после следует статистика
			else:
				#обновление статистики библиотеки
				new_lib.statistics.update(eval(line))
		print(info)
		t.close()
		#из массива info информация сохраняется в саму библиотеку
		new_lib.name = info[1]
		new_lib.version = info[2]
		new_lib.reliability = float(info[3])
		new_lib.maxwords = int(info[4])
		if info[5] == "LOCKED":
			new_lib.lock = True
		libraries.append(new_lib)
		print("A new library called '" + new_lib.name + "' is successfuly saved.")
		print("Would you like to use this library now?")
		print("yes_no >>>\n")
		a = yes_no(input())
		#библиотека может быть использована сразу
		if a:
			settings.library = libraries[-1]
			print("The changes are applied, you may type 'info' to check them.")
		else:
			print("You may apply it later by typing 'change_lib'.")
	#файл библиотеки не найден или не может быть прочитан
	except IOError or EOFError:
		print("Error: there is no appropriate *.libt file in the directory. You now will return home.")

#функция изменения статистики при самообучении
def didaction(tex , libr):
	#статистика хранится в словаре stats
	stats = libr.statistics
	#for i in range(libr.maxwords):
	#обновление статистики библиотеки
	for i in range(len(tex) - 1):
		#слово уже сохранено в библиотеке
		if tex[i] in stats:
			#после него уже сохранено слово
			if tex[i+1] in stats[tex[i]]:
				#в таком случае счетчик этой комбинации увеличивается
				stats[tex[i]][tex[i+1]] += 1
				#libr.reliability увеличивается - при увеличении библиотеки её рейтинг повышается
				libr.reliability = 1.0 - (1.0-libr.reliability)*(100 * len(stats) / (100 * len(stats)+3))
			#после него не употреблялось данное слово
			else:
				#в таком случае новая комбинация будет добавлена со счетчиком 1
				stats[tex[i]][tex[i+1]] = 1
				libr.reliability = 1.0 - (1.0-libr.reliability)*(50 * len(stats) / (50 * len(stats)+1))
		#слово не сохранено в библиотеке
		else:
			#в таком случае новое и следующее за ним слова будут добавлены
			stats[tex[i]] = {tex[i+1] : 1}
			libr.reliability = 1.0 - (1.0-libr.reliability)*(30 * len(stats) / (30 * len(stats)+1))

#поиск предложенного слова на основе библиотеки
def word_output(word , libr):
	stats = libr.statistics
	for vr in stats[word]:
		best = vr
		break
	for vr in stats[word]:
		#выбирается комбинация с самым большим счетчиком
		if stats[word][vr] > stats[word][best]:
			best = vr
	return(best)

#нажатие на слово в окне (beta)
def btn_clicked(button):
	global settings
	global word_output
	global word
	if word in settings.library.statistics:
		button['text'] = word_output(word, settings.library)
	else:
		button['text'] = ". . ."

#работа с окном (beta)
def cloth():
	global word_output
	global settings
	global root
	global buttons
	global btn_clicked
	global word
	for i in range(settings.showwords):
		new_btn = Button(root)
		buttons.append(new_btn)
		new_btn.configure(text="...", command=btn_clicked(new_btn))


"""
========================================================================================================================================
CONSOLE LAUNCHER:
========================================================================================================================================
"""

#лаунчер - работа с программой через консоль
def start(command): 
	global settings
	global commands_info
	global libraries
	global version
	global builtin_libs
	global LIBRARY
	global word
	global new_lib_dialog
	global yes_no
	global didaction
	global change_lib
	global new_lib
	global restore_lib
	global restore_file
	global run_text
	global word_output

	#помощь - список доступных команд с пояснениями
	if command == "help" or command == "Help":
		print("Here is the list of available commands:")
		for c in commands_info:
			print(c , "-" , commands_info[c])

	#информация - действующие настройки
	elif command == "info" or command == "Info":
		print("Here is the information about current settings:")
		print(settings.name)
		print("Statistics library:" , settings.library.name)
		print("Statistics reliability:" , str(int(settings.library.reliability * 10000) / 100) + "%")
		print("Words offered:" , str(settings.showwords))
		print("Machine learning mode:" , settings.autodidact)
		print("Version:" , version , "/" , settings.library.version)

	#библиотеки - список всех установленных библиотек
	elif command == "libraries" or command == "libs":
		if len(libraries):
			print("Here is the list of existing statistics libraries:")
			for lib in libraries:
				print(lib.name)
		else:
			print("No libraries yet, but you can create one now")

	#новый файл самообучения - создание пустого текстового файла формата *.adid
	elif command == "new_adid":
		print("Type in the name of the new machine learning file. Example: Great_Gatsby.")
		print("new_adid >>>\n")
		filename = input() + ".adid"
		l = open(filename , 'w')
		l.close()
		print(filename , "is successfully saved to the  app directory.")

	#смена библиотеки
	elif command == "change_lib":
		change_lib()

	#создание библиотеки
	elif command == "new_lib":
		new_lib_dialog()

	#самообучение на файле
	elif command == "run_text":
		run_text()

	#восстановление библиотеки из файла
	elif command == "restore_lib":
		restore_lib()

	#восстановление предустановленных библиотек - см далее
	elif command == "restore_def":
		restore_def(builtin_libs)

	#редактирование библиотеки
	elif command == "edit_lib":
		edit_lib()

	#изменение настроек
	elif command in {"edit_sets" , "edit_settings"}:
		edit_sets()

	#выход из лаунчера
	elif command in {"stop_console" , "close_dialogue" , "quit"}:
		return(1)

	#поиск в статистике библиотеки по слову
	elif (command[0] == "'" or command[0] == '"') and (command[-1] == "'" or command[-1] == '"'):
		word = command[1 : -1]
		if word in settings.library.statistics:
			print(word_output(word , settings.library))
		else:
			print("No such word in current library.")

	#нет такой команды
	else:
		print("There is no similar command. It may appear in the following versions.")
		print("You may type 'help' to see possible commands.")
		print("home >>>\n")
		return(start(input()))

	return(0)

print("Input command or library word in 'quotes'.")
print("Type 'help' to see possible commands or 'info' to see current settings.")

#восстановление предустановленных библиотек
def restore_def(builtin_libs):
	global LIBRARY
	global libraries
	global restore_file
	global yes_no
	possible = []
	#поиск доступных файлов библиотек
	for name in builtin_libs:
		try:
			t = open(name + ".libt" , 'rt')
			possible.append(name)
			t.close()
		except IOError or EOFError:
			libr = LIBRARY()
			libr.name = name
			libraries.append(libr)
			restore_file(libr)
	if len(possible):
		if len(possible) == 1:
			print("\nThere is one built-in library in the archive - " , possible[0] , ".\nWould you like to restore it?")
		else:
			print("\nThere are " + str(len(possible)) + " built-in libraries in the archive: " , possible , "\nWould you like to restore them?")
		if yes_no(input()):
			print("yes_no >>>\n")
			#поочередная установка библиотек
			for name in possible:
				info = []
				inf = True
				print(name + " unpacking...")
				#более подробно установка библиотек описана в разделе restore_lib
				try:
					t = open(name + ".libt" , 'rt')
					new_lib = LIBRARY()
					new_lib.name = name
					new_lib.statistics = {}
					for line in t:
						if inf:
							info.extend(line.split())
							if info[-1] == "info>":
								inf = False
						else:
							new_lib.statistics.update(eval(line))
					t.close()
					new_lib.name = info[1]
					new_lib.version = info[2]
					new_lib.reliability = float(info[3])
					new_lib.maxwords = int(info[4])
					if info[5] == "LOCKED":
						new_lib.lock = True
					libraries.append(new_lib)
					print("Library added.\n")
				#файл не найден или не может быть прочитан
				except IOError or EOFError:
					print("Error\n")
		else:
			print("You can restore them later by typing 'restore_lib' or 'restore_def'.")

restore_def(builtin_libs)
cloth()
end = 0
while not end:
	for btn in buttons:
		btn.pack()
	#за один запуск лаунчер обрабатывает только одну команду, поэтому лаунчер работает в цикле
	print("home >>>\n")
	end = start(input())

root.mainloop()
