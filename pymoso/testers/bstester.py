# MIT License

# Copyright (c) 2018 Kyle Cooper and Susan Hunter

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Summary
-------
Provide the tester for the Bus Scheduling problem.
"""
from ..problems import bsprob
from math import sqrt


def get_ranx0(rng):
	"""
	Uniformly sample from the feasible space.

	Parameters
	----------
	rng : prng.MRG32k3a object

	Returns
	-------
	x0 : tuple of int
		The randomly chosen point
	"""
	tau = 100
	q = 9
	mr = range(tau)
	x0 = tuple(rng.choice(mr) for i in range(q))
	return x0


def true_g(x):
	"""
	Compute the expected values of a point.

	Parameters
	----------
	x : tuple of int
		A feasible point

	Returns
	-------
	tuple of float
		The objective values
	"""
	lambd = 10
	q = 9
	c0 = 100
	tau = 100
	xext = list(x).extend([0, tau])
	xsrt = sorted(xext)
	obj1 = 0
	obj2 = 0
	for i in range(1, q + 1):
		indic = xsrt[i] - xsrt[i - 1]
		pass_cost = sqrt(lamd*indic) if indic > 0 else 0
		fixed_cost = c0*indic if indic > 0 else 0
		obj1 += pass_cost + fixed_cost
		obj2 += indic**2
	return obj1, obj2*(lambd/2.0)


class BSTester(object):
	"""
	Store useful data for working with the Bus Scheduling problem

	Attributes
	----------
	ranorc : chnbase.Oracle class, BSProb
	true_g : function, true_g
	get_ranx0 : function, get_ranx0
	"""
	def __init__(self):
		self.ranorc = bsprob.BSProb
		#self.answer = myanswer
		self.true_g = true_g
		self.get_ranx0 = get_ranx0

	def metric(self, eles):
		"""
		Compute a metric from a simulated solution to the true solution. For
		the Bus scheduling problem, the true solution is unkown and this
		function exists to allow using the testsolve command.

		Parameters
		----------
		eles : set of tuple of numbers
			Simulated solution

		Returns
		-------
		float
			The performance metric
		"""
		return 0
