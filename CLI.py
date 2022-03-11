import os

# general variables
online = True

# Commands
def cd(param):
    #x = param[0]
    os.chdir(param)
    
def ls():
	x = os.listdir()
	for y in x:
		print(y)

def pwd():
    print(os. getcwd())

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
dict = {"pwd":pwd, "test":test1, "cd":cd, "ls":ls}

while online:
    com_raw = input("> ").split(" ")
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