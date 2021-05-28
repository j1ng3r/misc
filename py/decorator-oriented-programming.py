from curry import curry as c

(_print, print) = (print, None)
(_input, dinput) = (input, None)

# @c
# def pipe(fn, proc, x):
# 	_print(x)
# 	_print(fn(x))
# 	return proc(fn(x))

def pipe(fn):
	_print(fn)
	def collect(proc):
		def call(arg):
			_print(arg)
			_print(fn(arg))
			return proc(fn(arg))
		_print(call)
		_print(call(["hello", "worl"]))
		return call
	return collect

@c
def print(proc, arg):
	_print(arg)
	return None

@c
def method(prop, proc, arg, /, *, args = []):
	val = getattr(arg, prop)(*(args)) or arg
	_print(val)
	_print(proc)
	_print(proc(val))
	return proc(val)

@c
def dinput(val, proc):
	return proc(_input(val))

@dinput("> ")
@method("split", args=[" "])
@method("reverse")
@pipe(" ".join)
@print
def _(): pass
