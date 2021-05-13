def to_string(A):
	return "".join(A)

brackets = [
	"()",
	"[]",
	"{}",
]
binary = [
	"+-",
	"*/",
	"^",
]
unary = "+-"

all_brackets = to_string(brackets)
all_binary = to_string(binary)
all_symbols = all_brackets + all_binary + unary

class Operator:
	op_name = None
	vals = ()
	fns = {}
	def fill(self, v):
		raise Exception("Unimplemented function.")
	
	def eval(self):
		return self.fns[self.op_name](*map(lambda v: v.eval() if isinstance(v, Operator) else v, self.vals))
	
	def __str__(self):
		valstr = str(self.vals[0]) if len(self.vals) == 1 else "(" + str(self.vals[0]) + ", " + str(self.vals[1]) + ")"
		return valstr + " |> " + self.op_name

class Unary(Operator):
	vals = (None, )
	fns = {
		"+": lambda v: v,
		"-": lambda v: -v,
	}
	def fill(self, v):
		self.vals = (v, )

class Binary(Operator):
	vals = (None, None)
	level = -1
	fns = {
		"+": lambda u, v: u + v,
		"-": lambda u, v: u - v,
		"*": lambda u, v: u * v,
		"/": lambda u, v: u / v,
		"^": lambda u, v: u ** v,
	}
	def fill(self, v):
		self.vals = (self.vals[0], v)


def bin_precedes(op_bin, op_any):
	if isinstance(op_any, Binary): return op_bin.level <= op_any.level
	return isinstance(op_any, Unary)

def get_binary_level(token):
	level = 0
	for ops in binary:
		if token in ops:
			return level
		level += 1

def string2tokens(string):
	tokens = []
	acc = ""
	for char in string:
		if not char.isspace():
			if char in all_symbols:
				if acc != "":
					tokens.append(acc)
					acc = ""
				tokens.append(char)
			else:
				acc += char
	if acc != "":
		tokens.append(acc)
	return tokens

def tokens2AST(tokens):
	opStack = []
	val = None
	for token in tokens:
		if token in all_brackets:
			for bracketPair in brackets:
				if token in bracketPair:
					if token is bracketPair[0]:
						if val is not None: raise Exception("Cannot have value before bracket.")
						opStack.append(bracketPair[1])
						break
					elif token is bracketPair[1]:
						if val is None: raise Exception("Empty or uncompleted bracket internals.")
						
						while not isinstance(lastOp := opStack[-1], str):
							lastOp.fill(val)
							val = lastOp
							opStack.pop()
							if len(opStack) == 0: raise Exception("Trailing bracket.")
						
						if lastOp is not token: raise Exception("Mismatched bracket.")
						
						opStack.pop()
		elif val is None and token in unary:
			op = Unary()
			op.op_name = token
			opStack.append(op)
		elif val is not None and token in all_binary:
			op = Binary()
			op.op_name = token
			op.level = get_binary_level(token)
			
			while bin_precedes(op, lastOp := opStack[-1] if len(opStack) > 0 else None):
				lastOp.fill(val)
				val = lastOp
				opStack.pop()
			
			op.vals = (val, None)
			val = None
			opStack.append(op)
		else:
			if val is not None: raise Exception("Two values in a row at token " + token + ".")
			val = float(token)
	
	if val is None: raise Exception("Trailing operator.")
	
	lastOp = opStack[-1] if len(opStack) > 0 else None
	while lastOp is not None:
		if isinstance(lastOp, str): raise Exception("Leading bracket.")
		lastOp.fill(val)
		val = lastOp
		opStack.pop()
		lastOp = opStack[-1] if len(opStack) > 0 else None # There's got to be a way to put this inside the while loop condition
	
	return val

def str2AST(string):
	return tokens2AST(string2tokens(string))

import sys

AST = str2AST(sys.argv[1])
print(str(AST))
print(AST.eval())
