#def myFun(*argv):
#    for arg in argv:
#       print(arg)
# myFun("ok" , "there", "you", "go")

#def myFun(arg1, *argv):
#	print(arg1)
#	for arg in argv:
#		print(arg)


#myFun("ok" , "there", "you", "go")
def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


myFun(first='hey', mid='you', last='there')
def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)
args = ("hey", "you", "there")
myFun(*args)

kwargs = {"arg1": "now", "arg2": "i can", "arg3": "see you"}
myFun(**kwargs)
def myFun(*args, **kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)

myFun('i', 'am', 'nobody', first="who", mid="you", last="are")


