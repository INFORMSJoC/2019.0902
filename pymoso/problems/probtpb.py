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

#!/usr/bin/env python
"""
Summary
-------
Provides implementation of the Test Problem B Oracle for use in PyMOSO.
"""
from ..chnbase import Oracle
from math import exp


class ProbTPB(Oracle):
    """
    An Oracle that simulates Test Problem B.

    Attributes
    ----------
    num_obj : int, 2
    dim : int, 2

    Parameters
    ----------
    rng : prng.MRG32k3a object

    See also
    --------
    chnbase.Oracle
    """
    def __init__(self, rng):
        self.num_obj = 2
        self.dim = 2
        super().__init__(rng)

    def g(self, x, rng):
        """
        Simulates one replication. PyMOSO requires that all valid
        Oracles implement an Oracle.g.

        Parameters
        ----------
        x : tuple of int
        rng : prng.MRG32k3a object

        Returns
        -------
        isfeas : bool
        tuple of float
            simulated objective values
        """
        obj1 = None
        obj2 = None
        isfeas = True
        xr = range(0, 101)
        for xi in x:
            if not xi in xr:
                isfeas = False
        if isfeas:
            z1 = rng.normalvariate(0, 1)
            z2 = rng.normalvariate(0, 1)
            xi = (z1**2, z2**2)
            g1 = 4*x[0]/100
            if x[1] >= 0 and x[1] <= 40:
                f2 = 4 - 3*exp(-pow((x[1]-20)/2, 2))
            else:
                f2 = 4 - 2*exp(-pow((x[1]-70)/20, 2))
            alpha = 0.25 + 3.75*(f2 - 1)
            if g1 <= f2:
                h = 1 - pow(g1/f2, alpha)
            else:
                h = 0
            obj2 = xi[0]*g1
            obj1 = xi[0]*xi[1]*f2*h
        return isfeas, (obj1, obj2)
