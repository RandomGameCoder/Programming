


def f(x=None,y=None):
	fun = "{x}+2*{y}"
	if x is None and y is None:
		return fun
	elif x is None or y is None:
		print("Error")
	else:
		print(eval(fun.format(x=x,y=y)))
        
