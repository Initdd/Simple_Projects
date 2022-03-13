import os
import shutil

# general variables
online = True
user = "user_1"

# Commands
def cat(file):
	fil = open(file, "r")
	print(fil.read())
	fil.close()
	
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
	
def rm(*param):
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
	
def touch(name):
	file = open(name, "w")
	file.close()
	
def mkdir(name):
	os.makedirs(name)

def cd(param):
    try:
        os.chdir(param)
    except:
        print(f"no file named \"{param}\"")
    
def ls():
	x = os.listdir()
	for y in x:
		print(y)

def pwd():
    print(os.getcwd())

def test1(*params):
    full = ""
    if len(params) > 3:
        print(len(params))
        print("too many paramters")
    else:
        for x in params:
            full += x
        print(full)

# Dict
dict = {"pwd":pwd, "test":test1, "cd":cd, "ls":ls, "cat":cat, "mkdir":mkdir, "touch":touch, "clear":clear, "rm":rm}

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
                print("too few arguments were given")
        else:
            del com_raw[0]
            dict.get(main)(*com_raw)
    else:
        print("command invalid")
