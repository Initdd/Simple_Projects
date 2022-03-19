import os
import shutil

# general variables
online = True
user = "user_1"

# Commands
def cat(*params):
	if "-h" in params:
		print("read a text based file")
	else:
		fil = open(params[0], "r")
		print(fil.read())
		fil.close()

def help():
	for item in dict:
		if item == "help":
			pass
		else:
			print(item)
	
def clear(*params):
    if "-h" in params:
    	print("clear terminal")
    else:
    	if os.name == "nt":
        	os.system("cls")
    	else:
        	os.system("clear")
	
def rm(*param):
    if "-h" in param:
    	print("remove files/directories\n-D for directories\nnothing for files (plus name of the file, obviously)")
    else:
    	if len(param) == 2 and param[1] == "-D":
        	try:
	        	os.rmdir(param[0])
        	except:
        	   	x = input("warn: directory not empty. want do delete anyway?(Y/N) ")
        	   	if x == "y" or x == "Y":
        	   	   shutil.rmtree(param[0])
        	   	else:
        	   		print("operation canceled")
    	else:
        	try:
        		os.remove(param[0])
        	except:
        		print("not a file")
	
def touch(*params):
	if "-h" in params:
		print("create empty file")
	else:
		file = open(params[0], "w")
		file.close()
	
def mkdir(*params):
	if "-h" in params:
		print("create folder")
	else:
		os.makedirs(params[0])

def cd(*params):
    if "-h" in params:
    	print("change current directory")
    else:
    	try:
        	os.chdir(params[0])
    	except:
        	print(f"no file named \"{param[0]}\"")
    
def ls(*params):
	x = os.listdir()
	if "-h" in params:
		print("list items in current directory")
	else:
		for y in x:
			print(y)

def pwd(*params):
    if "-h" in params:
    	print("print working directory")
    else:
    	print(os.getcwd())

def test1(*params):
    full = ""
    if "-h" in params:
    	print("-----------------------\ntest command help menu\n-----------------------")
    else:
    	if len(params) > 3:
    	  	 print(len(params))
    	  	 print("too many paramters")
    	else:
    	   	    for x in params:
    	   	    	full += x
    	   	    print(full)

# Dict
dict = {"help":help, "pwd":pwd, "test":test1, "cd":cd, "ls":ls, "cat":cat, "mkdir":mkdir, "touch":touch, "clear":clear, "rm":rm}

while online:
    # location
    loc = os.getcwd().split("/")
    if len(loc) == 1:
        location = f"/{loc[0]}"
    else:
        location = f"/{loc[len(loc)-2]}/{loc[len(loc)-1]}"

    com_raw = input(f"{user}@{location} $ ").split(" ")
    main = com_raw[0]
    if main in dict:
        if len(com_raw) == 1:
            try:
                dict.get(main)()
            except:
                pass
                print("too few arguments were given")
        else:
            del com_raw[0]
            dict.get(main)(*com_raw)
    else:
        print("command invalid")