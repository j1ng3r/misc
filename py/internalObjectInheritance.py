removeDuplicates = lambda l : list(set(l))

class base:
	class State:
		base = "base"

	def __init__(self):
		states = [c.State for c in type.mro(self.__class__) if c != object]
		class completeState(*removeDuplicates(states)): pass
		self.state = completeState()

class derived_alpha(base):
	class State:
		alpha = "alpha"

class derived_beta(derived_alpha):
	class State:
		beta = "beta"

class derived_gamma(derived_alpha):
	class State:
		gamma = "gamma"

class derived_delta(derived_beta, derived_gamma):
	pass

base = base()
delta = derived_delta()

print(delta.state.base)
print(delta.state.alpha)
print(delta.state.beta)
print(delta.state.gamma)
